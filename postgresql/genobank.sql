CREATE TABLE public.patients(
    id SERIAL NOT NULL,
    name varchar,
    idnumber varchar NOT NULL,
    investigator varchar,
    lab_logo varchar,
    lab_name varchar,
    test varchar,
    test_result varchar,
    test_date varchar,
    email varchar,
    created_at timestamp without time zone DEFAULT timezone('UTC'::text, now()) NOT NULL,
    updated_at timestamp without time zone DEFAULT timezone('UTC'::text, now()) NOT NULL
);

CREATE TABLE public.genoma(
    id SERIAL NOT NULL,
    jsondata varchar,
    consent varchar,
    test_type varchar,
    file_stored varchar,
    created_at timestamp without time zone DEFAULT timezone('UTC'::text, now()) NOT NULL,
    updated_at timestamp without time zone DEFAULT timezone('UTC'::text, now()) NOT NULL
);