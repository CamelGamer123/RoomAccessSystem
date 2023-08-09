# Database

This file details the documentation for the database, its different tables, and the methods in the database class.

## Tables

### AccessLogs 

This table stores the access logs for different rooms. The following table details the columns in the table.

| Column Name | Data Type | Description                                  |
|-------------|-----------|----------------------------------------------|
| id          | Integer   | The ID of the access log.                    |
| userId      | Integer   | The ID of the user that accessed the system. |
| inTime      | DateTime  | The time the user entered the room.          |
| outTime     | DateTime  | The time the user left the room.             |
| roomId      | Integer   | The ID of the room the user accessed.        |

### Rooms

This table stores the rooms in the system. The following table details the columns in the table.

| Column Name | Data Type | Description                                  |
|-------------|-----------|----------------------------------------------|
| id          | Integer   | The ID of the room.                          |
| blockCode   | String    | The block code of the room.                  |
| roomNumber  | String    | The room number of the room.                 |
| roomType    | String    | The type of room.                            |
| notes       | String    | Any notes about the room.                    |

### Users

The users table is not included in this system, as this system is designed to interface with the existing government
database.

A user id is in the following format: `<first letter of first name><first four letters of last name><unique number 
(begins at 0 and increments with every user with the same name in the system)>`. For example, the user id for John Smith
would be `jsmit0`. The user id for Jane Smith would be `jsmit1`.

## Database Class

The database class is used to interface with the database. The following table details the methods in the database class.

| Method Name           | Parameters                      | Return Type       | Description                                                            |
|-----------------------|---------------------------------|-------------------|------------------------------------------------------------------------|
| addAccessLog          | userId, roomId, inTime, outTime | None              | Adds an access log to the database.                                    |
| getAccessLogs         | None                            | List of AccessLog | Returns a list of all access logs in the database.                     |
| getAccessLogsByUserId | userId                          | List of AccessLog | Returns a list of all access logs in the database for a specific user. |
| getAccessLogsByRoomId | roomId                          | List of AccessLog | Returns a list of all access logs in the database for a specific room. |

Note that when an access log is created, the outTime is set to `None`. This is because the user has not left the room yet.
When the user leaves the room, the outTime is updated to the time the user left the room. If it is not updated, the
outTime will remain as `None`. Events such as fire alarms will deactivate the system and leave the outTime as `None`. 
Additionally, there is a mechanism in place to prevent a user from becoming trapped in a room if the system is deactivated
and the user is still in the room.

## AccessLog Class

The AccessLog class is used to represent an access log in the database. The following table details the attributes in the
AccessLog class. 

| Attribute Name | Data Type | Description                                  |
|----------------|-----------|----------------------------------------------|
| id             | Integer   | The ID of the access log.                    |
| userId         | Integer   | The ID of the user that accessed the system. |
| inTime         | DateTime  | The time the user entered the room.          |
| outTime        | DateTime  | The time the user left the room.             |
| roomId         | Integer   | The ID of the room the user accessed.        |

