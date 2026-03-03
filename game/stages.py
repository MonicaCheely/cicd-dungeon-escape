stages = [
    {
        "name": "Goblin Gate – Build Failure",
        "monster": "Goblin",
        "ascii_art": r"""
           ,      ,
          /(.-""-.)\
      |\  \/      \/  /|
      | \ / =.  .= \ / |
      \( \   o\/o   / )/
       \_, '-/  \-' ,_/
         /   \__/   \
         \ \__/\__/ /
       ___\ \|--|/ /___
     /`    \      /    `\
        """,
        "narrative": "A sneaky goblin blocks the dungeon gate. The build fails because a dependency is missing.",
        "technical": "Missing dependencies prevent builds. CI ensures all dependencies are declared to keep downstream stages stable.",
        "options": {"A": "Restart the CI server.","B": "Install and declare the missing dependency.","C": "Comment out the failing import."},
        "answer": "B",
        "hint": "Dependencies are the key to opening the gate.",
        "teaching": {"A": "Wrong: Restarting won’t fix missing dependencies.","B": "Correct: Installing dependencies keeps the build stable.","C": "Wrong: Hiding imports only delays the problem."}
    },
    {
        "name": "Skeleton Bridge – Test Failure",
        "monster": "Skeleton",
        "ascii_art": r"""
        .-.
       (o.o)
        |=|
       __|__
     //.=|=.\\
    // .=|=. \\
    \\ .=|=. //
     \\(_=_)//
      (:| |:)
       || ||
       () ()
       || ||
       || ||
      ==' '==
        """,
        "narrative": "A rickety skeleton bridge collapses under failing tests.",
        "technical": "Unit tests catch bugs early. CI uses a clean environment to prevent 'works on my machine' errors.",
        "options": {"A": "Skip failing tests.","B": "Fix the failing tests.","C": "Force merge the code."},
        "answer": "B",
        "hint": "Tests keep your path safe.",
        "teaching": {"A": "Wrong: Ignoring tests leads to unstable builds.","B": "Correct: Fixing tests ensures CI reliability.","C": "Wrong: Force merging risks breaking main."}
    },
    {
        "name": "Orc Forge – Docker Build",
        "monster": "Orc",
        "ascii_art": r"""
        ,   A           {}
       / \, | ,        .--.
      |    =|= >      /.--.\
       \ /` | `       |====|
        `   |         |`::`|
            |     .-;`\..../`;_.-^-._
           /\\\\/  /  |...::..|`   :   `|
           |:'\ |   /'''::''|   .:.   |
            \ /\;-,/\   ::  |..:::::..|
            |\ <` >  >._::_.| ':::::' |
            | `""`  /   ^^  |   ':'   |
            |       |       \    :    /
            |       |        \   :   /
        """,
        "narrative": "A fiery orc prevents your Docker container from building.",
        "technical": "Container builds must succeed; incorrect Dockerfile or missing files cause failures.",
        "options": {"A": "Fix the Dockerfile configuration.","B": "Add more memory and retry.","C": "Use 'latest' tags blindly."},
        "answer": "A",
        "hint": "Correct the container configuration.",
        "teaching": {"A": "Correct: Proper Dockerfile ensures consistent builds.","B": "Wrong: Memory won’t fix config issues.","C": "Wrong: Blind tags don’t solve build errors."}
    },
    {
        "name": "Troll Tunnel – Merge Conflicts",
        "monster": "Troll",
        "ascii_art": r"""
       /  _  \
      |  O O  |
      |   L   |
      |  ___  |
       \_____/
        """,
        "narrative": "A troll blocks your tunnel with merge conflicts.",
        "technical": "Merge conflicts occur when code changes collide. Resolving them ensures clean merges.",
        "options": {"A": "Override the branch blindly.","B": "Manually resolve conflicts.","C": "Delete the branch."},
        "answer": "B",
        "hint": "Carefully resolve the conflicts.",
        "teaching": {"A": "Wrong: Overriding loses work.","B": "Correct: Manual resolution keeps all intended changes.","C": "Wrong: Deleting branch discards work."}
    },
    {
        "name": "Elf’s Hollow – Environment Issue",
        "monster": "Elf",
        "ascii_art": r"""
        /\  /\
       ( o\/o )
        \    /
         |==|
         || ||
         || ||
        """,
        "narrative": "A mischievous elf alters your staging environment.",
        "technical": "Environment inconsistencies cause staging failures; match environments to prevent surprises.",
        "options": {"A": "Ignore staging errors.","B": "Sync environments and fix the issue.","C": "Deploy directly to production."},
        "answer": "B",
        "hint": "Align the environments.",
        "teaching": {"A": "Wrong: Ignoring errors risks broken code.","B": "Correct: Syncing environments ensures consistency.","C": "Wrong: Deploying broken code is dangerous."}
    },
    {
        "name": "Spider Lair – Security Scan",
        "monster": "Giant Spider",
        "ascii_art": r"""
          (\     /)
          ( \\---// )
           ) . . (
          (  =^=  )
           )     (
          /       \
         (         )
        (           )
       ( (  )   (  ) )
        """,
        "narrative": "A giant spider has woven vulnerabilities into your web of code!",
        "technical": "Security scans detect vulnerabilities before deployment; ignoring them risks attacks.",
        "options": {"A": "Skip the scan.","B": "Fix security vulnerabilities.","C": "Hide the reports."},
        "answer": "B",
        "hint": "Defeat vulnerabilities to proceed.",
        "teaching": {"A": "Wrong: Skipping risks breaches.","B": "Correct: Fixing vulnerabilities keeps production safe.","C": "Wrong: Hiding issues does not fix them."}
    },
    {
        "name": "Wolf Den – Configuration Error",
        "monster": "Wolf",
        "ascii_art": r"""
        /\_/\  
       ( o.o ) 
        > ^ <
        """,
        "narrative": "A hungry wolf freezes your configuration files, making deployments impossible.",
        "technical": "Misconfigurations break deployments; proper configuration management prevents surprises.",
        "options": {"A": "Deploy anyway.","B": "Correct the configuration files.","C": "Remove configuration files."},
        "answer": "B",
        "hint": "Check config files carefully.",
        "teaching": {"A": "Wrong: Deploying broken configs fails the release.","B": "Correct: Fixing configuration ensures deployment success.","C": "Wrong: Removing configs creates more problems."}
    },
    {
        "name": "Fluffy’s Lair – Monitoring Failure",
        "monster": "Fluffy the Cerberus",
        "ascii_art": r"""
          ,     ,
         /(.•_•.)\
         \   |   /
         /   |   \
        (___/ \___)
        Fluffy guards your monitoring dashboards!
        """,
        "narrative": "Fluffy the Cerberus hides critical alerts in your monitoring system.",
        "technical": "Monitoring detects problems early; fixing monitoring ensures quick response.",
        "options": {"A": "Ignore alerts.","B": "Fix monitoring and alerts.","C": "Turn off monitoring."},
        "answer": "B",
        "hint": "See what Fluffy is guarding.",
        "teaching": {"A": "Wrong: Ignoring alerts allows issues to escalate.","B": "Correct: Fixing monitoring ensures problems are caught early.","C": "Wrong: Turning off monitoring is dangerous."}
    },
    {
        "name": "Server Crypt – Performance Bottleneck",
        "monster": "Skeleton Mage",
        "ascii_art": r"""
         .-.
        (o.o)
         |=|
        __|__
       //.=|=.\\
      // .=|=. \\
      \\ .=|=. //
       \\(_=_)//
        (:| |:)
         || ||
         () ()
        """,
        "narrative": "A skeleton mage slows down your server with heavy computations.",
        "technical": "Performance issues can crash deployments; profiling and optimizing is key.",
        "options": {"A": "Ignore performance warnings.","B": "Optimize the slow code.","C": "Restart the server frequently."},
        "answer": "B",
        "hint": "Optimize the slow parts.",
        "teaching": {"A": "Wrong: Ignoring slows everything down.","B": "Correct: Optimization improves performance.","C": "Wrong: Restarting is not a fix."}
    },
    {
        "name": "Dragon’s Lair – Deployment Catastrophe",
        "monster": "Dragon",
        "ascii_art": r"""
                      __====-_  _-====___
               _--^^^#####//      \\#####^^^--_
            _-^##########// (    ) \\##########^-_
           -############//  |\^^/|  \\############-
         _/############//   (@::@)   \\############\_
        /#############((     \\//     ))#############\
       -###############\\    (oo)    //###############-
      -#################\\  / UUU \  //#################-
     -###################\\/  (v)  \/###################-
    _#/|##########/\######(   /   \   )######/\##########|\#_
    |/ |#/\#/\#/\/  \#/\##\  |(_ ^ _)|  /##/\#/  \/\#/\#/\| \|
        """,
        "narrative": "The mighty dragon blocks your final deployment! One wrong move could burn production.",
        "technical": "Deployment failures can take down production. Rollback or fix issues safely.",
        "options": {"A": "Redeploy blindly.","B": "Roll back to the last stable version.","C": "Ignore the failure and continue."},
        "answer": "B",
        "hint": "Defeat the dragon safely by rolling back.",
        "teaching": {"A": "Wrong: Blind redeploy risks production.","B": "Correct: Rolling back protects production while fixing issues.","C": "Wrong: Ignoring failure is catastrophic."}
    }
]