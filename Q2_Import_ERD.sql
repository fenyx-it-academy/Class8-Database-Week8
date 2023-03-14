CREATE TABLE public.Member (
	"member_id" serial NOT NULL,
	"team_id" integer NOT NULL,
	"member_name" VARCHAR(255) NOT NULL,
	"member_title" VARCHAR(255) NOT NULL,
	"member_email" VARCHAR(255) NOT NULL,
	CONSTRAINT "Member_pk" PRIMARY KEY ("member_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE public.Team (
	"team_id" serial NOT NULL,
	"team_name" VARCHAR(255) NOT NULL,
	"number_of_member" integer NOT NULL,
	CONSTRAINT "Team_pk" PRIMARY KEY ("team_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE public.Product (
	"product_id" serial NOT NULL,
	"team_id" integer NOT NULL,
	"product_name" VARCHAR(255) NOT NULL,
	"product_desc" VARCHAR(255) NOT NULL,
	"domain_id" integer NOT NULL,
	CONSTRAINT "Product_pk" PRIMARY KEY ("product_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE public.Customer (
	"customer_id" integer NOT NULL,
	"customer_name" VARCHAR(255) NOT NULL,
	"customer_phone" VARCHAR(255) NOT NULL,
	CONSTRAINT "Customer_pk" PRIMARY KEY ("customer_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE public.Domain (
	"domain_id" serial NOT NULL,
	"domain_name" VARCHAR(255) NOT NULL,
	"customer_id" integer NOT NULL,
	CONSTRAINT "Domain_pk" PRIMARY KEY ("domain_id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "Member" ADD CONSTRAINT "Member_fk0" FOREIGN KEY ("team_id") REFERENCES Team("team_id");


ALTER TABLE "Product" ADD CONSTRAINT "Product_fk0" FOREIGN KEY ("team_id") REFERENCES Team("team_id");
ALTER TABLE "Product" ADD CONSTRAINT "Product_fk1" FOREIGN KEY ("domain_id") REFERENCES Domain("domain_id");


ALTER TABLE "Domain" ADD CONSTRAINT "Domain_fk0" FOREIGN KEY ("customer_id") REFERENCES Customer("customer_id");






