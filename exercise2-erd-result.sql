CREATE TABLE "public.Teams" (
	"team_id" serial NOT NULL,
	"product_id" serial NOT NULL,
	"team_name" TEXT NOT NULL,
	CONSTRAINT "Teams_pk" PRIMARY KEY ("team_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Members" (
	"member_id" serial NOT NULL,
	"team_id" serial NOT NULL,
	"first_name" TEXT NOT NULL,
	"last_name" TEXT NOT NULL,
	"title" TEXT NOT NULL,
	CONSTRAINT "Members_pk" PRIMARY KEY ("member_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Products" (
	"product_id" serial NOT NULL,
	"product_name" TEXT NOT NULL,
	"customer_id" serial NOT NULL,
	CONSTRAINT "Products_pk" PRIMARY KEY ("product_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Customers" (
	"customer_id" serial NOT NULL,
	"customer_name" TEXT NOT NULL,
	"customer_domain" TEXT NOT NULL,
	CONSTRAINT "Customers_pk" PRIMARY KEY ("customer_id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "public.Teams" ADD CONSTRAINT "Teams_fk0" FOREIGN KEY ("product_id") REFERENCES "public.Products"("product_id");

ALTER TABLE "public.Members" ADD CONSTRAINT "Members_fk0" FOREIGN KEY ("team_id") REFERENCES "public.Teams"("team_id");

ALTER TABLE "public.Products" ADD CONSTRAINT "Products_fk0" FOREIGN KEY ("customer_id") REFERENCES "public.Customers"("customer_id");






