# Setting up the Slackbot

The first step is to create and set up a new Slackbot:

1. [Create](https://slack.com/create) a Slack workspace for testing the bot.
2. Go to the Slack [app directory](https://api.slack.com/apps) and click `Create New App`.
3. Create a name for the app (bot) and link it to the test workspace.

<img src="https://github.com/cw75/torchMojiBot/blob/master/images/slack-create.png" alt="drawing" width="650"/>

4. Go to the `OAuth & Permissions` tab and add `channels:history`, `im:history`, and `reactions:write` to the `Bot Token Scopes`.

<img src="https://github.com/cw75/torchMojiBot/blob/master/images/slack-auth.png" alt="drawing" width="650"/>

5. Click `Install App to Workspace` and `Allow`. You should see the `Bot User OAuth Access Token` after installation.

The next step is to deploy the torchMoji model. Proceed to [here](https://github.com/cw75/torchMojiBot/tree/master/deploy/sagemaker) if you want to deploy it on SageMaker, and [here](https://github.com/cw75/torchMojiBot/tree/master/deploy/algorithmia) if you want to deploy it on Algorithmia.


<br />
---------------------------------------------------------------------------------
<br /><br />

After deploying the model, Lambda function, and setting up the API gateway:

6. On the `Event Subscriptions` tab, subscribe to bot events `message.channels` and `message.im` and paste the API gateway's REST endpoint URL (in the form `https://unique-id.amazonaws.com/slack/events`) to the `Request URL` box. You should see the green text `Verified` with a checkmark, meaning Slack's [url verification](https://api.slack.com/events/url_verification) succeeded.

<img src="https://github.com/cw75/torchMojiBot/blob/master/images/slack-sub.png" alt="drawing" width="650"/>

You've now successfully deployed an AI-powered emoji bot to Slack, congradulations! See [here](https://github.com/cw75/torchMojiBot) for how to test the bot via direct messaging or adding the bot to channels. Have fun!
