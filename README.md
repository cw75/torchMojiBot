# torchMojiBot

This repo contains the code and detailed instruction to reproduce the intelligent Slackbot I built in this [blog post](https://towardsdatascience.com/how-i-built-a-deep-learning-powered-emoji-slackbot-5d3e59b76d0#229c-19e0b1a26b5b). Powered by the [torchMoji](https://github.com/cw75/torchMoji) model, the bot automatically reacts to Slack messages with emoji.

Before proceeding, make sure you have installed `python3` (the repo is tested with python3.6), `wget`, and `zip`.  
Also, install and configure [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

If you are deploying the model on SageMaker, you also need `docker` (installation guide [here](https://docs.docker.com/engine/install/)).  
If you are deploying the model on Algorithmia, you also need `pip3` (the repo is tested with pip3.6).

Overall, there are 5 steps:
1. Set up the Slackbot by completing steps 1-5 [here](https://github.com/cw75/torchMojiBot/tree/master/slack).
2. Deploy the torchMoji model on [SageMaker](https://aws.amazon.com/sagemaker/) or [Algorithmia](https://algorithmia.com/) (or both!). See [here](https://github.com/cw75/torchMojiBot/tree/master/deploy/sagemaker) for SageMaker deployment and [here](https://github.com/cw75/torchMojiBot/tree/master/deploy/algorithmia) for Algorithmia deployment.
3. Deploy the AWS Lambda function that performs request authentication and routes traffic between Slack and the prediction service. Instruction [here](https://github.com/cw75/torchMojiBot/tree/master/lambda).
4. Set up the API gateway that routes traffic to the Lambda function and exposes a REST endpoint to Slack. Instruction [here](https://github.com/cw75/torchMojiBot/tree/master/api-gateway).
5. Finish setting up the Slackbot by completing step 6 [here](https://github.com/cw75/torchMojiBot/tree/master/slack).

After completing all the steps above, send a direct message "this is great!" to your bot (not to yourself!) in the Slack workspace. You should see the following.

![Slack](https://github.com/cw75/torchMojiBot/blob/master/images/slack.png)

You can even add the bot to channels by doing the following:
1. Click "Apps" on your Slack workspace (upper-left) and click the name of your bot.
2. Click "Details" on the upper-right corner, click the "..." icon that says "More", and click "Add this app to a channel".
3. Select the channel you want the bot to join and click "Add".

In my case, I have added the bot to the "test" channel, and here we go:

![Slack-channel](https://github.com/cw75/torchMojiBot/blob/master/images/slack-channel.png)

When you are done having fun, remember to delete all the AWS resources you created to save $$$!
