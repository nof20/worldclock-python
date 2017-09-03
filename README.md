# worldclock-python

A simple Python/Flask app to test the process of building and deploying containers on Google Container Platform.

The app itself exposes a simple REST API to return the current time in seven different time zones, e.g.

```bash
$ curl localhost:8080/api/v1.0/time
{
  "America/New_York": "2017-09-03T18:46:29-0400",
  "Australia/Sydney": "2017-09-04T08:46:29+1000",
  "Europe/London": "2017-09-03T23:46:29+0100",
  "Europe/Zurich": "2017-09-04T00:46:29+0200",
  "Singapore": "2017-09-04T06:46:29+0800",
  "US/Eastern": "2017-09-03T18:46:29-0400",
  "US/Pacific": "2017-09-03T15:46:29-0700"
}
```

It also returns some simple info about the host the container is running on:

```bash
$ curl localhost:8080/api/v1.0/info
{
  "machine": "x86_64",
  "nodename": "55b2aace560a",
  "release": "4.9.41-moby",
  "sysname": "Linux",
  "timezone": "Etc/UTC",
  "version": "#1 SMP Fri Aug 18 01:58:38 UTC 2017"
}
```

### Build and run locally

First, [install Docker on your workstation](https://docs.docker.com/engine/installation/).

Then build and run locally:

```bash
$ docker build -t worldclock-python . ; docker run -p 8080:8080 worldclock-python
```

### Build and run on Google Container Platform

Before you begin, you must download and install the Google Cloud SDK, login,
create a project, and enable the Container Engine and Container Builder APIs. See instructions [here](https://cloud.google.com/container-engine/docs/quickstart).

To build the container:

```bash
$ gcloud container builds submit --config cloudbuild.yaml .
```

The container image is automatically named `worldclock-python` in the Container
Registry.  To create a Kubernetes cluster and run the image remotely on Google Container Engine:

```bash
$ gcloud config set compute/zone us-central1-b
$ gcloud container clusters create worldclock-python
$ kubectl run worldclock-python --image=gcr.io/<project-id>/worldclock-python --port=8080
$ kubectl expose deployment worldclock-python --type=“LoadBalancer"
$ kubectl get service worldclock-python
```
