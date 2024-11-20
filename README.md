# coildb

## Set up

`cd backend`
`python -m venv venv`

## Running
`oc login --web`

Usage:
- Run `make install` to install dependencies for both backend and frontend.
- Run `make test_backend` to test the Python backend.
- Run `make backend` to start the Python backend.
- Run `make frontend` to start the React frontend.
- Run `make all` to start both the backend and frontend concurrently in separate terminals if you're using a multiprocess terminal setup.

## Connecting to PostgreSQL Database and Creating a Test Table in OpenShift

This document outlines the steps to connect to a PostgreSQL database running on OpenShift, create a test table, and verify its functionality.

## Prerequisites

- Access to OpenShift CLI (`oc`) > use `oc login`
- Permissions to interact with the OpenShift project
- PostgreSQL instance running in your OpenShift project

## Steps to Connect to PostgreSQL and Create a Test Table

### 1. Connect to PostgreSQL Pod Using `psql`

1. **Find the Pod Name:**
   Run the following command to list the pods and find the PostgreSQL pod name:
   ```bash
   oc get pods
   ```

2. **Access the Pod:**
   Use the `oc rsh` command to connect to the PostgreSQL pod:
   ```bash
   oc rsh <your-postgresql-pod-name>
   ```

3. **Connect to PostgreSQL Using `psql`:**
   Inside the pod, connect to the PostgreSQL database with the following command:
   ```bash
   psql -U <POSTGRES_USER> -d <POSTGRES_DB>
   ```
   Replace `<POSTGRES_USER>` and `<POSTGRES_DB>` with the appropriate values (e.g., `dev_user` and `dev_db`).


### 2. Exit the `psql` Prompt and Pod

1. **Exit `psql`:**
   Type the following command to leave the `psql` prompt:
   ```sql
   \q
   ```

2. **Exit the Pod Shell:**
   Type `exit` to leave the pod shell.

---

You have now successfully connected to the PostgreSQL database, created a test table, and inserted data.
