CREATE TABLE public.teams (
	team_id serial NOT NULL,
	team_name varchar(255) NOT NULL,
	CONSTRAINT teams_pk PRIMARY KEY (team_id)
) WITH (
  OIDS=FALSE
);

CREATE TABLE public.products (
	product_id serial NOT NULL,
	product_name varchar(255) NOT NULL,
	product_description VARCHAR(255) NOT NULL,
	team_id integer NOT NULL,
	CONSTRAINT products_pk PRIMARY KEY (product_id)
) WITH (
  OIDS=FALSE
);

CREATE TABLE public.staff_members (
	staff_id serial NOT NULL,
	staff_name varchar(255) NOT NULL,
	team_id integer NOT NULL,
	title_id integer NOT NULL,
	CONSTRAINT staff_members_pk PRIMARY KEY (staff_id)
) WITH (
  OIDS=FALSE
);

CREATE TABLE public.member_responsibility (
	title_id serial NOT NULL,
	title_name varchar(255) NOT NULL,
	CONSTRAINT member_responsibility_pk PRIMARY KEY (title_id)
) WITH (
  OIDS=FALSE
);

CREATE TABLE public.customer (
	customer_id serial NOT NULL,
	customer_name varchar(255) NOT NULL,
	customer_address VARCHAR(255) NOT NULL,
	CONSTRAINT customer_pk PRIMARY KEY (customer_id)
) WITH (
  OIDS=FALSE
);

CREATE TABLE public.domain (
	domain_id serial NOT NULL,
	domain_name varchar(255) NOT NULL,
	domain_description VARCHAR(255) NOT NULL,
	CONSTRAINT domain_pk PRIMARY KEY (domain_id)
) WITH (
  OIDS=FALSE
);

CREATE TABLE public.product_customer (
	product_customer_id serial NOT NULL,
	customer_id integer NOT NULL,
	product_id integer NOT NULL,
	CONSTRAINT product_customer_pk PRIMARY KEY (product_customer_id)
) WITH (
  OIDS=FALSE
);

CREATE TABLE public.domain_customer (
	domain_customer_id serial NOT NULL,
	customer_id integer NOT NULL,
	domain_id integer NOT NULL,
	CONSTRAINT domain_customer_pk PRIMARY KEY (domain_customer_id)
) WITH (
  OIDS=FALSE
);

ALTER TABLE products ADD CONSTRAINT products_fk0 FOREIGN KEY (team_id) REFERENCES teams(team_id);
ALTER TABLE staff_members ADD CONSTRAINT staff_members_fk0 FOREIGN KEY (team_id) REFERENCES teams(team_id);
ALTER TABLE staff_members ADD CONSTRAINT staff_members_fk1 FOREIGN KEY (title_id) REFERENCES member_responsibility(title_id);
ALTER TABLE product_customer ADD CONSTRAINT product_customer_fk0 FOREIGN KEY (customer_id) REFERENCES customer(customer_id);
ALTER TABLE product_customer ADD CONSTRAINT product_customer_fk1 FOREIGN KEY (product_id) REFERENCES products(product_id);
ALTER TABLE domain_customer ADD CONSTRAINT domain_customer_fk0 FOREIGN KEY (customer_id) REFERENCES customer(customer_id);
ALTER TABLE domain_customer ADD CONSTRAINT domain_customer_fk1 FOREIGN KEY (domain_id) REFERENCES domain(domain_id);