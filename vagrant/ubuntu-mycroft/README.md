# mycroft

https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/macos-and-windows-with-virtualbox#installing-ubuntu-in-virtualbox

Meant to be used with <https://mycroft-ai.gitbook.io/docs/skill-development/introduction/your-first-skill>


Related project: (Minecraft game) <https://github.com/HenryFBP/mycroft-minecroft-text-game>

## Setup (if it didnt automatically do it from `vagrant up`)


    pushd ~/Git
        bash dev_setup.sh
    popd

Then you can run `vagrant up --provsion` to clone the repo,

and edit `/opt/mycroft/skills/mycroft-minecroft-text-game` with your favorite IDE. I like PyCharm.