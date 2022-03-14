CREATE TABLE public.patients(
    id SERIAL NOT NULL,
    name varchar,
    idnumber NOT NULL varchar,
    investigator varchar,
    lab_logo varchar,
    lab_name varchar,
    test varchar,
    test_result varchar,
    test_date varchar,
    created_at timestamp without time zone DEFAULT timezone('UTC'::text, now()) NOT NULL,
    updated_at timestamp without time zone DEFAULT timezone('UTC'::text, now()) NOT NULL
);