# B3 Notifier

A email notifier for B3 stock prices 💸 📈

## Installation

1. Clone this repository
2. Copy .env.sample, rename it to .env and populate it with data
3. Use `docker-compose up --build` to start the necessary containers and active the *Celery Schedule*
4. Wait to receive some awesome emails with prices 😃

## Supported APIs

Today this only fetches data from [HG Brasil Finace API][1], so in order to use it you will need a account.

Doesn't want to use this API or need the support for another one? Create a *Issue*! Or even better, fork this project and open a ***awesome*** *Pull Request*!


[1]: https://hgbrasil.com/status/finance
