# coildb

## Running the backend

From coildb:

`cd backend`

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python main.py`

## Running frontend

`cd frontend`

`npm install`

`npm start`

Here's a Markdown README document with the steps outlined for connecting to the PostgreSQL database, creating a test table, and inserting data.

---

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

### 2. Create a Test Table

1. **Run SQL Commands:**
   Once in the `psql` prompt, run this SQL command to create a test table:
   ```sql
   CREATE TABLE test_table (
       id SERIAL PRIMARY KEY,
       name VARCHAR(50) NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

2. **Verify the Table:**
   Run the following command to check that the table was created:
   ```sql
   \dt
   ```

### 3. Insert Test Data (Optional)

1. **Insert a Sample Record:**
   Add a sample entry to the table with this command:
   ```sql
   INSERT INTO test_table (name) VALUES ('Test Entry');
   ```

2. **View the Inserted Data:**
   Run the following command to display the data in the table:
   ```sql
   SELECT * FROM test_table;
   ```

### 4. Exit the `psql` Prompt and Pod

1. **Exit `psql`:**
   Type the following command to leave the `psql` prompt:
   ```sql
   \q
   ```

2. **Exit the Pod Shell:**
   Type `exit` to leave the pod shell.

---

You have now successfully connected to the PostgreSQL database, created a test table, and inserted data.
