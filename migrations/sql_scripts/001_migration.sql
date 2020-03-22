-- auto-migrations didn't auto-generate defaults for the columns
ALTER TABLE "user" ALTER COLUMN admin SET DEFAULT FALSE;
ALTER TABLE "user" ALTER COLUMN created_at SET DEFAULT (now() at time zone 'utc');

ALTER TABLE ingredient_stock ALTER COLUMN unit SET DEFAULT 4;
ALTER TABLE recipe_ingredient ALTER COLUMN unit SET DEFAULT 4;
