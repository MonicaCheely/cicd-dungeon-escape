stages = [
    {
        "name": "The Locked Gate – Build Failure",
        "narrative": (
            "The dungeon gate refuses to open.\n"
            "The build failed. A dependency went missing. No one admits touching it."
        ),
        "technical": (
            "During the build stage of a CI/CD pipeline, required dependencies "
            "are installed before packaging or compiling the application. "
            "If a dependency is missing, incorrectly versioned, or not declared "
            "in requirements.txt, the build process will fail and block all "
            "downstream stages. This ensures incomplete or unstable code does "
            "not move forward in the pipeline."
        ),
        "options": {
            "A": "Restart the CI server and hope it resolves itself.",
            "B": "Install and properly declare the missing dependency.",
            "C": "Comment out the failing import statement."
        },
        "answer": "B"
    },
    {
        "name": "The Shaking Floor – Test Failure",
        "narrative": (
            "The floor trembles beneath your feet.\n"
            "The tests passed locally… but CI says otherwise."
        ),
        "technical": (
            "Unit tests validate expected behavior before code is deployed. "
            "If tests pass locally but fail in CI, it often indicates "
            "environment inconsistencies, missing environment variables, "
            "uncommitted changes, or dependency mismatches. "
            "CI environments provide a clean and standardized execution space "
            "to prevent 'it works on my machine' scenarios."
        ),
        "options": {
            "A": "Disable the failing tests temporarily.",
            "B": "Investigate and fix the failing test cases.",
            "C": "Force merge the changes into main."
        },
        "answer": "B"
    },
    {
        "name": "The Smoking Forge – Docker Failure",
        "narrative": (
            "Smoke fills the chamber.\n"
            "The Docker image refuses to build. The forge is unstable."
        ),
        "technical": (
            "Containerization ensures consistent application environments "
            "across development, testing, and production. "
            "A Docker build failure typically results from errors in the "
            "Dockerfile, incorrect base images, missing files, or dependency "
            "installation issues. Fixing the Dockerfile ensures the container "
            "image builds reliably and can be deployed consistently."
        ),
        "options": {
            "A": "Review and correct the Dockerfile configuration.",
            "B": "Increase system memory and try again.",
            "C": "Use the 'latest' tag for all images without verification."
        },
        "answer": "A"
    },
    {
        "name": "The Final Bridge – Deployment Failure",
        "narrative": (
            "You reach the final bridge.\n"
            "The deployment stage failed. Production remains untouched."
        ),
        "technical": (
            "The deployment stage promotes tested code into a production "
            "environment. If deployment fails, it may be due to configuration "
            "errors, infrastructure issues, or failing health checks. "
            "A safe practice in DevOps is to roll back to the last stable "
            "version to prevent service disruption while investigating the root cause."
        ),
        "options": {
            "A": "Redeploy repeatedly until it works.",
            "B": "Roll back to the last stable version and investigate.",
            "C": "Announce success despite the failure."
        },
        "answer": "B"
    }
]