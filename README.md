# coildb

### The COIL Database is a full-stack web application which provides a user-friendly way to access and modify information required by the UNC Global Affairs staff to maintain the COIL program.

The COIL (Collaborative Online International Learning) Database is a web application designed by The Global Education Team to enhance how the UNC Global Affairs staff manages information related to COIL courses. The Global Education Team is the team of UNC Global Affairs staff members that manage the COIL Database. Currently, staff rely on Excel spreadsheets, which are prone to human errors and inconsistencies, especially due to user-created formulas. This new web based database will serve as an upgrade, offering a more structured and efficient way to input and manage course data. It will also introduce quality-of-life features, such as diagnostic tools and graphs to further streamline the management process.

The software is primarily for the UNC Global Education Team, who are divided into admins and team members. Admins will have the ability to add and update course information using intuitive forms, ensuring data accuracy. Meanwhile, team members will have access to view the data and generate reports either directly on the website or by exporting the data as CSV files. By distinguishing roles at login, the system ensures a seamless and secure experience, allowing admins to manage data effectively while users can view it without accidentally altering the database, making the process both efficient and error-free.

## Set up

`cd backend`
`python -m venv venv`

## Running

`oc login --web`

Usage:
- Run `make install` to install dependencies for both backend and frontend.
- Run `make test_backend` to run integration tests on the Python backend.
- Run `make backend` to start the Python backend.
- Run `make frontend` to start the React frontend.
- Run `make` to start both the backend and frontend concurrently in separate terminals if you're using a multiprocess terminal setup.

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


## Populate the Databases
To run SQL files in order to populate or alter the databases used the following piped command:
`cat <path to sql file> | oc rsh <psql pod> psql -d <db_name>`

The `<db_name>` will be `prod_db` for the production database pod and `dev_db` for the development database pod.

---

You have now successfully connected to the PostgreSQL database, created a test table, and inserted data.
