from sklearn.preprocessing import LabelEncoder

from entropy import behavioral_entropy, print_entropy 
import hmm_model
from parser import (
    read_screen_time,
    read_browser_history,
    read_mood_sleep
)
from triggers import (
    get_trigger
)

from intervention_engine import (
    run_intervention,
    update_intervention,
    print_intervention_report
)
from data_preparation import (
    prepare_features,
    split_dataset,
    print_dataset_information
)
from report_generator import generate_report
from context_switch import (
    calculate_context_switch_cost,
    print_context_switch_report
)

from behavioral_engine import (
    behavioral_engine,
    print_report
)
from life_graph import (
    build_life_graph,
    draw_graph,
    print_graph,
    graph_summary,
    top_transitions,
    save_graph
)
from sequence_mining import (
    recurring_loops,
    print_loops
)
from xgboost_model import (
    train_xgboost,
    predict,
    evaluate_model,
    save_model,
    plot_feature_importance
)
from hmm_model import (
    train_hmm,
    predict_states,
    print_states
)
from granger_causality import (
    prepare_granger_data,
    perform_granger_test,
    print_granger_summary
)
from prediction_comparison import (
    compare_models,
    print_comparison,
    plot_accuracy
)

from validation import validate_data
from feature_engineering import create_time_bucket
from database import create_table, insert_dataframe
from utils import print_title, download_nltk, tokenize_text


def main():

    print_title("LifeOS: Predicting Human Behavior")

    download_nltk()

    create_table()

    screen = read_screen_time("data/sample/screen_time.csv")

    browser = read_browser_history("data/sample/browser_history.csv")

    mood = read_mood_sleep("data/sample/mood_sleep.csv")

    screen = validate_data(screen)
    browser = validate_data(browser)
    mood = validate_data(mood)

    screen = screen.rename(
        columns={
            "App": "activity",
            "Date": "timestamp",
            "Duration": "duration"
        }
    )
    screen["category"] = "Digital"
    trigger = get_trigger(screen)

    action = run_intervention(trigger)
    X, y = prepare_features(screen)

    X_train, X_test, y_train, y_test = split_dataset( X,   y  )
 

    label_encoder = LabelEncoder()

    y_train = label_encoder.fit_transform(y_train)

    y_test = label_encoder.transform(y_test)

    print_dataset_information(
        X_train,
        X_test
)
    model = train_xgboost(
        X_train,
        y_train
)

    predictions = predict(
        model,
        X_test
)

    accuracy = evaluate_model(
        y_test,
        predictions
    )


    save_model(model)
    plot_feature_importance(
        model,
        X_train.columns
)
    activity_encoder = LabelEncoder()

    screen_hmm = screen.copy()

    screen_hmm["activity"] = activity_encoder.fit_transform(
    screen_hmm["activity"]
)

    hmm_model = train_hmm(screen_hmm)

    states = predict_states(
        hmm_model,
        screen_hmm
)

    print_states(states)
    granger_data = prepare_granger_data(screen)

    results = perform_granger_test(
        granger_data
)

    print_granger_summary(results)

    print("\n========== XGBoost ==========")
    
    print(f"Accuracy : {accuracy:.2%}")
    baseline_accuracy, hmm_accuracy = compare_models(
    accuracy
)

    print_comparison(
        baseline_accuracy,
        accuracy,
        hmm_accuracy
)

    plot_accuracy(
        baseline_accuracy,
        accuracy,
        hmm_accuracy
)
    context_cost = calculate_context_switch_cost(screen)

    print_context_switch_report(screen)

    entropy_score = behavioral_entropy(
    screen,
    "activity"
)

    screen = create_time_bucket(screen, "timestamp")

    insert_dataframe(
        screen[
            [
                "activity",
                "timestamp",
                "duration",
                "category",
                "source"
            ]
        ]
    )
    
    graph = build_life_graph(screen)
    print_graph(graph)

    graph_summary(graph)

    top_transitions(graph)

    save_graph(graph)

    draw_graph(graph)
    loops = recurring_loops(screen)

    print_loops(loops)
    report = behavioral_engine(screen)
    generate_report(
    entropy_score,
    context_cost,
    graph,
    loops
)
    responded = True

    update_intervention(
        action,
        responded
)

    print_intervention_report()

    print_report(report)
    
    print(screen.head())
    print_entropy(entropy_score)

    print("\nBrowser History")
    print(browser.head())

    print("\nMood Data")
    print(mood.head())
    print_entropy(entropy_score)

  #  print("\nNLTK Example:")
   # print(tokenize_text("LifeOS predicts human behaviour"))


if __name__ == "__main__":
    main()