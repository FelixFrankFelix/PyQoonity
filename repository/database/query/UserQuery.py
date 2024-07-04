

READ_BY_ID = "SELECT * FROM users WHERE user_id = :user_id AND user_status != 'DELETED'"
READ_BY_EMAIL = "SELECT * FROM users WHERE user_email = :user_email AND user_status != 'DELETED'"
READ_BY_NAME = "SELECT * FROM users WHERE user_name = :user_name AND user_status != 'DELETED'"
READ_ALL = "SELECT * FROM users WHERE user_status != 'DELETED' ORDER BY user_id"
CREATE = "INSERT INTO users (user_name, user_email, user_password, user_created_at, user_updated_at, user_status) VALUES (:user_name, :user_email, :user_password, :user_created_at, :user_updated_at, :user_status)"
UPDATE = "UPDATE users SET user_name = :user_name, user_email = :user_email,user_password = :user_password, user_updated_at = :user_updated_at, user_status = :user_status WHERE user_id = :user_id"
DELETE = "UPDATE users SET user_status = 'DELETED', user_updated_at = :user_updated_at WHERE user_id = :user_id"