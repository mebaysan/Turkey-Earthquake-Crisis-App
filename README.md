[![CI](https://github.com/mebaysan/Turkey-Earthquake-Crisis-App/actions/workflows/ci.yml/badge.svg)](https://github.com/mebaysan/Turkey-Earthquake-Crisis-App/actions/workflows/ci.yml) [![Update Docker Hub Description](https://github.com/mebaysan/Turkey-Earthquake-Crisis-App/actions/workflows/dockerhub-description.yml/badge.svg)](https://github.com/mebaysan/Turkey-Earthquake-Crisis-App/actions/workflows/dockerhub-description.yml)

# Introduction

I've created this [repo](https://github.com/mebaysan/Turkey-Earthquake-Crisis-App) to present a minimal crisis map for earhquakes in Turkey.

You can easily run the app by using [Docker](https://docker.com).


Thanks for [BOGAZICI UNIVERSITY KANDILLI OBSERVATORY AND EARTHQUAKE RESEARCH INSTITUTE (KOERI)](http://www.koeri.boun.edu.tr/scripts/lasteq.asp) sharing the data.

**Upon use of our data, proper attribution should be given to KOERI-RETMC in scientific articles and general purpose reports by referencing the network citation.**

# Docker Image on the Hub
Explore Image on Docker Hub: [mebaysan/turkey-earthquake-crisis-app](https://hub.docker.com/repository/docker/mebaysan/turkey-earthquake-crisis-app)

# Manual

```bash
docker run -p 8501:8501 mebaysan/turkey-earthquake-crisis-app
```