Thanks for opening up my phase-3 project at Flatiron School, CLI Multi-Lingual Bot.  In this project I explored the chatterbot engine and google translate API to create a command line chat bot.  If you would like to check out my project, you will need to set up a venv and download python 3.7.16.  Also, you will need the Google Could Translate API document I created for this project.  To get it, send me an email at:

    krieger.jacqueline@gmail.com

with the subject line as:

    CLIMulti-LingualBot Request

Also let me know somehow that you are a real human.

NOTE: Chatterbot is no longer maintained, so to get the lastest version that works with the required dependencies, it is important to follow these steps.  It is quite a process, but it is still possible to open this up and use it.  Follow these steps:

1. Get your local environment set up:

    a. If you know how to install python 3.7.16, go ahead and do that and set it to as your global version of python.  If you're not sure how to do that, follow these steps:

        + have homebrew already installed?  Great!  Skip this step.  If not, go to your command line and type the following:

            $ /bin/bash-c"$(curl - fsSL https://raw.githubusercontent.com/Homebres/install/head/install.sh)

        ++NOTE: It is going to ask for your password for admin access to your local machine.  It won't display any characters, but the system is tracking your input.  After you type it, hit enter and the install should start. 

        + Next, install the python version manager for your machine.  This will help you manage different versions of python, which is helpful for keeping different versions installed and swtiching between them.  Type:

            $ brew install pyenv

        + Next, find out what shell startup file (either .zshrc or .bash_profile) you are in.  Type: 

            $ echo $SHELL

        + You should see /bin/.zsh or /bin/.bash_profile.  Based on that type either:

            $ code ~/.bash_profile

        OR

            $ code ~/.zshrc

        This will open up the file in your code editor (assuming you have the code command installed in your editor.  If you do not, do a quick google search to find out how to do that, or open the file in whatever way you know how.)

        + add the following to the end of your file 

            if which pyenv > /dev/null; then 
                eval "$(pyenv init -)";
            fi

        + We want to load the new settings.  Type:

            $ source ~/.bash_profile
        
        or

            $ source ~/.zshrc
        
        + Now install our python version:

            $ pyenv install 3.7.16

        + Then set it as your global python version.  This is easy to change later, as you have not uninstalled other versions of python.  Type:

            $ pyenv global 3.7.16

2. Now you are going to fork this repo and clone it to your machine.  

2. Open it in your code editor.

3. Open the virtual enviromnent: 

    $ source venv/bin/activate

    You should now see (venv) in front of the line of code displaying your current location. 

4. Now we are going to install our dependencies.

    a. Install chatterbot version 1.0.4.  This one works with the necessary Natural Language Processing (NLP) libraries (most notably spacy and NLPTK) necesssary for making best-match responses:

        + Type:

            $ python -m pip install chatterbot==1.0.4 pytz

            This installs the version of chatterbot that we need, and the chatterbot corpus, in case you feel interested to use the corpus to train the bot further. 

    b. Install Google Cloud Translate.  I use this API to take the english training data I have fed the bot and translates the response to whatever laguage persona you have chosen to use. 

        + type:

            $ pip install google-cloud-translate.  
        
        + Now you should have the emailed API file.  Go ahead and create a new file titled this:  
        
        simple_bot_api.json 
        
        This should allow you to access the API.  

        + To see a list of installed dependencies you can type:

            $ python -m pip freeze
        
        Here you should see chatterbot and google cloud translate, along with many other dependencies.  If those two are there you should be good.

5. Now you are going to open the file to begin the login in process in the command line:

    $ python CLI_new_user.py

5. create a new user by providing username, password and email.

6. select the language you want the bot to respond in, and start chatting.  

If you have any questions, send me an email and I will be happy to help out.  Thank you!