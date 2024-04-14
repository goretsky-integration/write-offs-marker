# Write-offs marker

Listen to events of ingredient write-offs and mark them as written off.

--- 

### ⚙️ Setup

#### 1. Clone repository and setup virtual environment

```shell
git clone https://github.com/goretsky-integration/write-offs-marker
cd write-offs-marker

poetry env use python3.11
poetry shell
poetry install --without dev
```

---

#### 2. Create config file

```shell
cp config.example.toml config.toml
```

--- 

#### 3. Fill in the fields in the `config.toml` file.

Set up timezone.

`credentials_file_path` - path to the file with google service account credentials.
<details>
<summary>How to get credentials?</summary>

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate
and be authorized to access data in Google APIs.

Since it’s a separate account, by default it does not have access to any spreadsheet until you share it with this
account. Just like any other Google account.

#### Here’s how to get one:

1. Enable API Access for a Project if you haven’t done it yet.
    <details>
    <summary>🤔 How do I enable API Access?</summary>
    Enable API Access for a Project
    Head to Google Developers Console and create a new project (or select the one you already have).

   In the box labeled “Search for APIs and Services”, search for “Google Drive API” and enable it.

   In the box labeled “Search for APIs and Services”, search for “Google Sheets API” and enable it.
    </details>
2. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
3. Fill out the form
4. Click “Create” and “Done”.
5. Press “Manage service accounts” above Service Accounts.
6. Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new
   key”.
7. Select JSON key type and press “Create”.

You will automatically download a JSON file with credentials. It may look like this:

```json
{
  "type": "service_account",
  "project_id": "api-project-XXX",
  "private_key_id": "2cd … ba4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
  "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
  "client_id": "473 … hd.apps.googleusercontent.com"
}
```

Remember the path to the downloaded credentials file. Also, in the next step you’ll need the value of client_email from
this file.

Very important! Go to your spreadsheet and share it with a client_email from the step above. Just like you do with any
other Google account.

If you don’t do this, you’ll get a `gspread.exceptions.SpreadsheetNotFound` exception when trying to
access this spreadsheet from your application or a script.
</details>

---

`spreadsheet_key` - you can get it from the URL of spreadsheet.

```toml
[google_sheets]
credentials_file_path = "/file/to/credentials.json"
spreadsheet_key = "jfsodijfiosdjijsfigjfg"
```

---

URL of the message queue which will be listened to events.

```toml
[message_queue]
url = "amqp://localhost:5672"
```

---

Telegram bot token for answering to callback queries.

```toml
[telegram_bot]
token = "12345:gkdfgifdjgifdjgfdg"
```

---

#### 4. Run the service

```shell
cd src
faststream run main:app
```
