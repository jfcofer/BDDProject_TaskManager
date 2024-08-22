CREATE TYPE status AS ENUM ('Completado', 'En Progreso', 'Pendiente');
CREATE TYPE priority AS ENUM (
    'P1',
    'P2',
    'P3',
    'P4'
);
CREATE TABLE IF NOT EXISTS 'user' (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS report (
    id SERIAL PRIMARY KEY,
    creation_date DATE NOT NULL,
    user_id INT NOT NULL REFERENCES 'user' (id),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS task (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE,
    current_status status NOT NULL DEFAULT 'Pendiente',
    current_priority priority NOT NULL DEFAULT 'Prioridad 1',
    user_id INT NOT NULL REFERENCES user (id),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS subtask (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    current_status status NOT NULL DEFAULT 'Pendiente',
    current_priority priority NOT NULL DEFAULT 'Prioridad 1',
    main_task_id INT NOT NULL REFERENCES task (id),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS reminder (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    reminder_date DATE NOT NULL,
    task_id INT NOT NULL REFERENCES task (id),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);