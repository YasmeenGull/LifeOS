$correctName = "Yasmeen Gull"
$correctEmail = "gullyasmeen814@gmail.com"

$commits = git rev-list --all

foreach ($commit in $commits) {
    git filter-branch -f --env-filter @"
if [ "`$GIT_COMMIT" = "$commit" ]; then
    export GIT_AUTHOR_NAME="$correctName"
    export GIT_AUTHOR_EMAIL="$correctEmail"
    export GIT_COMMITTER_NAME="$correctName"
    export GIT_COMMITTER_EMAIL="$correctEmail"
fi
"@ $commit^..HEAD
}