--
-- PostgreSQL database cluster dump
--

\restrict WIRCwcRU6VlQV4fEYWdebBp5NieEdrGnJnPWvfCzSrmLf8KBumzlcG2uNgpvGHz

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Drop databases (except postgres and template1)
--

DROP DATABASE django_linebot;




--
-- Drop roles
--

DROP ROLE "postgresAdmin";


--
-- Roles
--

CREATE ROLE "postgresAdmin";
ALTER ROLE "postgresAdmin" WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:jQFglk3UPvnT7sa/nCg1nw==$qJKAJSS568a/2bu6t7zbKqPeXITY5rKaa5Wi6Xcdaj8=:eM6bA56Ta3GhoKOBP6xHxR2DgpnkkEWhcV1wECJYggY=';

--
-- User Configurations
--








\unrestrict WIRCwcRU6VlQV4fEYWdebBp5NieEdrGnJnPWvfCzSrmLf8KBumzlcG2uNgpvGHz

--
-- Databases
--

--
-- Database "template1" dump
--

--
-- PostgreSQL database dump
--

\restrict ZaDPxtKQ18uDdmHDxWX754Xsmc1JxKHiKN9UuvCEz9Z2lsyH4XbNLIlEIxuyXO5

-- Dumped from database version 16.14 (Debian 16.14-1.pgdg13+1)
-- Dumped by pg_dump version 16.14 (Debian 16.14-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

UPDATE pg_catalog.pg_database SET datistemplate = false WHERE datname = 'template1';
DROP DATABASE template1;
--
-- Name: template1; Type: DATABASE; Schema: -; Owner: postgresAdmin
--

CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE template1 OWNER TO "postgresAdmin";

\unrestrict ZaDPxtKQ18uDdmHDxWX754Xsmc1JxKHiKN9UuvCEz9Z2lsyH4XbNLIlEIxuyXO5
\connect template1
\restrict ZaDPxtKQ18uDdmHDxWX754Xsmc1JxKHiKN9UuvCEz9Z2lsyH4XbNLIlEIxuyXO5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: COMMENT; Schema: -; Owner: postgresAdmin
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: template1; Type: DATABASE PROPERTIES; Schema: -; Owner: postgresAdmin
--

ALTER DATABASE template1 IS_TEMPLATE = true;


\unrestrict ZaDPxtKQ18uDdmHDxWX754Xsmc1JxKHiKN9UuvCEz9Z2lsyH4XbNLIlEIxuyXO5
\connect template1
\restrict ZaDPxtKQ18uDdmHDxWX754Xsmc1JxKHiKN9UuvCEz9Z2lsyH4XbNLIlEIxuyXO5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: ACL; Schema: -; Owner: postgresAdmin
--

REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


--
-- PostgreSQL database dump complete
--

\unrestrict ZaDPxtKQ18uDdmHDxWX754Xsmc1JxKHiKN9UuvCEz9Z2lsyH4XbNLIlEIxuyXO5

--
-- Database "django_linebot" dump
--

--
-- PostgreSQL database dump
--

\restrict W0DoGhD6jOrvHLc01dyxWj0UM4ZyC2BK8T1dREaHKizfdHxzIrSQ0Rl3fllTGDa

-- Dumped from database version 16.14 (Debian 16.14-1.pgdg13+1)
-- Dumped by pg_dump version 16.14 (Debian 16.14-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: django_linebot; Type: DATABASE; Schema: -; Owner: postgresAdmin
--

CREATE DATABASE django_linebot WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE django_linebot OWNER TO "postgresAdmin";

\unrestrict W0DoGhD6jOrvHLc01dyxWj0UM4ZyC2BK8T1dREaHKizfdHxzIrSQ0Rl3fllTGDa
\connect django_linebot
\restrict W0DoGhD6jOrvHLc01dyxWj0UM4ZyC2BK8T1dREaHKizfdHxzIrSQ0Rl3fllTGDa

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgresAdmin
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO "postgresAdmin";

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgresAdmin
--

COMMENT ON SCHEMA public IS '';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO "postgresAdmin";

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO "postgresAdmin";

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO "postgresAdmin";

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO "postgresAdmin";

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO "postgresAdmin";

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.auth_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.auth_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO "postgresAdmin";

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO "postgresAdmin";

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO "postgresAdmin";

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO "postgresAdmin";

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO "postgresAdmin";

--
-- Name: favorite_stock; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.favorite_stock (
    id bigint NOT NULL,
    stock_id character varying(100) NOT NULL,
    user_account bigint NOT NULL
);


ALTER TABLE public.favorite_stock OWNER TO "postgresAdmin";

--
-- Name: COLUMN favorite_stock.user_account; Type: COMMENT; Schema: public; Owner: postgresAdmin
--

COMMENT ON COLUMN public.favorite_stock.user_account IS '對應Person id';


--
-- Name: favorite_stock_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.favorite_stock ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.favorite_stock_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: hot_stock; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.hot_stock (
    id bigint NOT NULL,
    stock_id character varying(100) NOT NULL,
    stock_name character varying(200) NOT NULL,
    suffix character varying(50) NOT NULL
);


ALTER TABLE public.hot_stock OWNER TO "postgresAdmin";

--
-- Name: COLUMN hot_stock.suffix; Type: COMMENT; Schema: public; Owner: postgresAdmin
--

COMMENT ON COLUMN public.hot_stock.suffix IS '.TW 或 .TWO';


--
-- Name: hot_stock_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.hot_stock ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.hot_stock_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: latest_news; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.latest_news (
    id bigint NOT NULL,
    title character varying(230) NOT NULL,
    url character varying(500),
    scraped_at timestamp with time zone NOT NULL
);


ALTER TABLE public.latest_news OWNER TO "postgresAdmin";

--
-- Name: latest_news_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.latest_news ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.latest_news_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: message; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.message (
    id bigint NOT NULL,
    keyword character varying(200) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    user_account bigint NOT NULL
);


ALTER TABLE public.message OWNER TO "postgresAdmin";

--
-- Name: message_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.message ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.message_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: person; Type: TABLE; Schema: public; Owner: postgresAdmin
--

CREATE TABLE public.person (
    id bigint NOT NULL,
    user_account character varying(150) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.person OWNER TO "postgresAdmin";

--
-- Name: person_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresAdmin
--

ALTER TABLE public.person ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.person_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add person	7	add_person
26	Can change person	7	change_person
27	Can delete person	7	delete_person
28	Can view person	7	view_person
29	Can add message	8	add_message
30	Can change message	8	change_message
31	Can delete message	8	delete_message
32	Can view message	8	view_message
33	Can add latest news	9	add_latestnews
34	Can change latest news	9	change_latestnews
35	Can delete latest news	9	delete_latestnews
36	Can view latest news	9	view_latestnews
37	Can add hot stock	10	add_hotstock
38	Can change hot stock	10	change_hotstock
39	Can delete hot stock	10	delete_hotstock
40	Can view hot stock	10	view_hotstock
41	Can add favorite stock	11	add_favoritestock
42	Can change favorite stock	11	change_favoritestock
43	Can delete favorite stock	11	delete_favoritestock
44	Can view favorite stock	11	view_favoritestock
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	basic_info	person
8	basic_info	message
9	crawler	latestnews
10	stock	hotstock
11	stock	favoritestock
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2026-07-07 03:38:21.605591+00
2	auth	0001_initial	2026-07-07 03:38:21.832543+00
3	admin	0001_initial	2026-07-07 03:38:21.917053+00
4	admin	0002_logentry_remove_auto_add	2026-07-07 03:38:21.953075+00
5	admin	0003_logentry_add_action_flag_choices	2026-07-07 03:38:21.977478+00
6	contenttypes	0002_remove_content_type_name	2026-07-07 03:38:22.008837+00
7	auth	0002_alter_permission_name_max_length	2026-07-07 03:38:22.019577+00
8	auth	0003_alter_user_email_max_length	2026-07-07 03:38:22.033859+00
9	auth	0004_alter_user_username_opts	2026-07-07 03:38:22.048317+00
10	auth	0005_alter_user_last_login_null	2026-07-07 03:38:22.065677+00
11	auth	0006_require_contenttypes_0002	2026-07-07 03:38:22.073946+00
12	auth	0007_alter_validators_add_error_messages	2026-07-07 03:38:22.092093+00
13	auth	0008_alter_user_username_max_length	2026-07-07 03:38:22.125376+00
14	auth	0009_alter_user_last_name_max_length	2026-07-07 03:38:22.150995+00
15	auth	0010_alter_group_name_max_length	2026-07-07 03:38:22.166033+00
16	auth	0011_update_proxy_permissions	2026-07-07 03:38:22.188338+00
17	auth	0012_alter_user_first_name_max_length	2026-07-07 03:38:22.218329+00
18	basic_info	0001_initial	2026-07-07 03:38:22.265567+00
19	crawler	0001_initial	2026-07-07 03:38:22.287799+00
20	sessions	0001_initial	2026-07-07 03:38:22.368153+00
21	stock	0001_initial	2026-07-07 03:38:22.46435+00
22	stock	0002_rename_user_account_favoritestock_user_account_id	2026-07-08 00:39:38.779286+00
23	stock	0002_alter_favoritestock_user_account	2026-07-08 00:51:40.528744+00
24	stock	0003_hotstock_suffix	2026-07-09 06:33:58.703556+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: favorite_stock; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.favorite_stock (id, stock_id, user_account) FROM stdin;
2	2330	1
3	00919	1
5	2441	1
\.


--
-- Data for Name: hot_stock; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.hot_stock (id, stock_id, stock_name, suffix) FROM stdin;
1	2330	台積電	TW
2	2317	鴻海	TW
3	2454	聯發科	TW
4	2308	台達電	TW
5	2882	國泰金	TW
6	2881	富邦金	TW
7	2412	中華電	TW
8	2603	長榮	TW
9	2615	萬海	TW
10	2609	陽明	TW
11	2303	聯電	TW
12	3711	日月光投控	TW
13	3037	欣興	TW
14	2382	廣達	TW
15	2357	華碩	TW
16	3231	緯創	TW
17	6669	緯穎	TW
18	2891	中信金	TW
19	0050	元大台灣50	TW
20	00878	國泰永續高股息	TW
21	6488	環球晶	TWO
22	3105	穩懋	TWO
23	8299	群聯	TWO
24	6274	台燿	TWO
25	5347	世界	TWO
26	00919	群益台灣精選高息	TW
27	2441	GREATEK ELECTRONICS INC	TW
\.


--
-- Data for Name: latest_news; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.latest_news (id, title, url, scraped_at) FROM stdin;
\.


--
-- Data for Name: message; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.message (id, keyword, created_at, user_account) FROM stdin;
1	股票0050	2026-07-07 05:37:17.862642+00	1
2	股票2330	2026-07-07 05:50:46.514744+00	1
3	股票00919	2026-07-07 06:35:30.034142+00	1
4	我的股票	2026-07-08 00:27:44.549849+00	1
5	我的股票	2026-07-08 00:43:07.725963+00	1
6	我的股票	2026-07-08 00:54:47.716515+00	1
7	我的股票	2026-07-08 00:56:40.244509+00	1
8	股票0050	2026-07-08 00:58:12.662784+00	1
9	我的股票	2026-07-08 01:05:09.057654+00	1
10	我的股票	2026-07-08 01:06:10.544265+00	1
11	我的股票	2026-07-08 01:07:53.00676+00	1
12	我的股票	2026-07-08 01:16:21.281012+00	1
13	我的股票	2026-07-08 01:16:48.216481+00	1
14	我的股票	2026-07-08 01:19:46.308342+00	1
15	我的股票	2026-07-08 01:20:52.831648+00	1
16	我的股票	2026-07-08 01:21:26.328273+00	1
17	我的股票	2026-07-08 01:22:39.389246+00	1
18	我的股票	2026-07-08 01:24:56.368379+00	1
19	我的股票	2026-07-08 01:25:39.524992+00	1
20	我的股票	2026-07-08 01:25:53.831592+00	1
21	我的股票	2026-07-08 01:32:12.891732+00	1
22	我的股票	2026-07-08 01:40:23.592155+00	1
23	我的股票	2026-07-08 01:41:15.351626+00	1
24	我的股票	2026-07-08 01:42:15.934008+00	1
25	我的股票	2026-07-08 01:45:23.016689+00	1
26	我的股票	2026-07-08 01:47:19.031003+00	1
27	我的股票	2026-07-08 01:51:50.920759+00	1
28	我的股票	2026-07-08 01:55:29.093784+00	1
29	我的股票	2026-07-08 02:13:46.758946+00	1
30	股票5274	2026-07-08 02:15:57.85807+00	1
31	股票0050	2026-07-08 02:17:05.751844+00	1
32	股票5274	2026-07-08 02:17:17.125856+00	1
33	股票5274	2026-07-08 02:18:42.047794+00	1
34	股票5274	2026-07-08 02:19:04.016803+00	1
35	股票5274	2026-07-08 02:21:04.273897+00	1
36	股票5274	2026-07-08 02:21:22.162654+00	1
37	股票5274	2026-07-08 05:39:34.574023+00	1
38	股票2330	2026-07-08 05:39:42.61046+00	1
39	股票2330	2026-07-08 05:42:26.043704+00	1
40	股票5274	2026-07-08 05:42:43.961518+00	1
41	股票5274	2026-07-08 05:44:24.18937+00	1
42	股票2330	2026-07-08 05:44:34.62082+00	1
43	股票5274	2026-07-08 05:45:49.36833+00	1
44	股票清單	2026-07-09 05:52:15.683769+00	1
45	我的股票	2026-07-09 05:52:28.763001+00	1
46	股票2330	2026-07-09 05:53:42.719561+00	1
47	股票5274	2026-07-09 06:02:05.868962+00	1
48	股票5274	2026-07-09 06:03:08.257705+00	1
49	股票2330	2026-07-09 06:03:18.968356+00	1
50	股票5274	2026-07-09 06:04:33.657148+00	1
51	股票0050	2026-07-09 06:04:43.663026+00	1
52	股票2330	2026-07-09 06:04:54.90323+00	1
53	股票2330	2026-07-09 06:05:15.895886+00	1
54	股票5274	2026-07-09 06:05:22.395515+00	1
55	股票5274	2026-07-09 06:05:54.124381+00	1
56	股票5274	2026-07-09 06:06:21.040903+00	1
57	股票0056	2026-07-09 06:06:29.995536+00	1
58	股票2330	2026-07-09 06:06:37.992289+00	1
59	股票2330	2026-07-09 06:06:50.846236+00	1
60	股票5274	2026-07-09 06:06:57.271918+00	1
89	股票5274	2026-07-09 06:25:49.018828+00	1
90	股票2330	2026-07-09 06:25:56.517551+00	1
91	股票5347	2026-07-09 06:42:24.987542+00	1
92	股票5347	2026-07-09 06:42:48.833363+00	1
93	股票2330	2026-07-09 06:42:57.992713+00	1
94	股票2330	2026-07-09 06:48:19.060499+00	1
95	我的股票	2026-07-09 06:49:16.780019+00	1
96	我的股票	2026-07-09 06:50:01.598757+00	1
97	我的股票	2026-07-09 06:50:36.365552+00	1
98	我的股票	2026-07-09 06:51:30.756+00	1
99	我的股票	2026-07-09 06:52:16.802869+00	1
100	我的股票	2026-07-09 06:52:55.257994+00	1
101	我的股票	2026-07-14 05:47:17.320465+00	1
102	我的股票	2026-07-14 05:48:48.951693+00	1
103	我的股票	2026-07-14 05:49:29.377079+00	1
104	我的股票	2026-07-14 05:53:39.034328+00	1
105	我的股票	2026-07-14 05:56:34.8631+00	1
106	我的股票	2026-07-14 05:57:11.54528+00	1
107	我的股票	2026-07-14 05:58:13.326867+00	1
108	我的股票	2026-07-14 05:59:56.790522+00	1
109	我的股票	2026-07-14 06:07:06.815629+00	1
110	我的股票	2026-07-14 06:13:13.289536+00	1
111	我的股票	2026-07-14 06:22:22.56509+00	1
112	股票00919	2026-07-14 06:23:02.439888+00	1
113	股票00919	2026-07-14 06:24:25.645546+00	1
114	股票00919	2026-07-14 06:28:17.02429+00	1
115	我的股票	2026-07-14 06:28:26.955959+00	1
116	股票00919	2026-07-16 01:53:51.650556+00	1
117	股票00919	2026-07-16 01:54:59.1736+00	1
118	股票00919	2026-07-16 01:55:26.375325+00	1
119	股票00919	2026-07-16 01:56:23.000534+00	1
120	股票00919	2026-07-16 01:57:15.786078+00	1
121	股票00919	2026-07-16 01:57:51.239758+00	1
122	股票00919	2026-07-16 01:58:09.307943+00	1
123	股票00878	2026-07-16 01:58:45.815175+00	1
124	股票2441	2026-07-16 02:02:49.894603+00	1
125	股票2441	2026-07-16 02:03:31.074781+00	1
126	股票2441	2026-07-16 02:04:33.864073+00	1
127	股票2441	2026-07-16 02:05:46.547646+00	1
128	股票2441	2026-07-16 02:07:21.496345+00	1
129	股票2441	2026-07-16 02:09:23.716395+00	1
130	股票2441	2026-07-16 02:10:11.307371+00	1
131	股票2441	2026-07-16 02:16:22.370889+00	1
132	股票2441	2026-07-16 02:17:45.32246+00	1
133	股票2441	2026-07-16 02:18:26.070297+00	1
134	股票2441	2026-07-16 02:18:58.763186+00	1
135	股票2441	2026-07-16 02:21:36.09253+00	1
136	股票2441	2026-07-16 02:29:21.918779+00	1
137	股票2441	2026-07-16 02:30:24.897045+00	1
138	股票2441	2026-07-16 02:31:19.659286+00	1
139	股票2441	2026-07-16 02:31:32.887374+00	1
140	股票2441	2026-07-16 02:35:25.722804+00	1
\.


--
-- Data for Name: person; Type: TABLE DATA; Schema: public; Owner: postgresAdmin
--

COPY public.person (id, user_account, created_at, updated_at) FROM stdin;
1	U22d0930e1913b65468996b2433bd0590	2026-07-07 03:59:12.572876+00	2026-07-07 03:59:12.572892+00
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 44, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 11, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 24, true);


--
-- Name: favorite_stock_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.favorite_stock_id_seq', 37, true);


--
-- Name: hot_stock_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.hot_stock_id_seq', 27, true);


--
-- Name: latest_news_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.latest_news_id_seq', 1, false);


--
-- Name: message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.message_id_seq', 140, true);


--
-- Name: person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgresAdmin
--

SELECT pg_catalog.setval('public.person_id_seq', 1, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: favorite_stock favorite_stock_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.favorite_stock
    ADD CONSTRAINT favorite_stock_pkey PRIMARY KEY (id);


--
-- Name: favorite_stock favorite_stock_stock_id_key; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.favorite_stock
    ADD CONSTRAINT favorite_stock_stock_id_key UNIQUE (stock_id);


--
-- Name: hot_stock hot_stock_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.hot_stock
    ADD CONSTRAINT hot_stock_pkey PRIMARY KEY (id);


--
-- Name: hot_stock hot_stock_stock_id_key; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.hot_stock
    ADD CONSTRAINT hot_stock_stock_id_key UNIQUE (stock_id);


--
-- Name: latest_news latest_news_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.latest_news
    ADD CONSTRAINT latest_news_pkey PRIMARY KEY (id);


--
-- Name: message message_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.message
    ADD CONSTRAINT message_pkey PRIMARY KEY (id);


--
-- Name: person person_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (id);


--
-- Name: person person_user_account_key; Type: CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_user_account_key UNIQUE (user_account);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: favorite_stock_stock_id_9143e420_like; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX favorite_stock_stock_id_9143e420_like ON public.favorite_stock USING btree (stock_id varchar_pattern_ops);


--
-- Name: favorite_stock_user_account_51ddbdd0; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX favorite_stock_user_account_51ddbdd0 ON public.favorite_stock USING btree (user_account);


--
-- Name: hot_stock_stock_id_da5d02a9_like; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX hot_stock_stock_id_da5d02a9_like ON public.hot_stock USING btree (stock_id varchar_pattern_ops);


--
-- Name: message_user_account_9d71759a; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX message_user_account_9d71759a ON public.message USING btree (user_account);


--
-- Name: person_user_account_0aef3474_like; Type: INDEX; Schema: public; Owner: postgresAdmin
--

CREATE INDEX person_user_account_0aef3474_like ON public.person USING btree (user_account varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: favorite_stock favorite_stock_user_account_51ddbdd0_fk_person_id; Type: FK CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.favorite_stock
    ADD CONSTRAINT favorite_stock_user_account_51ddbdd0_fk_person_id FOREIGN KEY (user_account) REFERENCES public.person(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: message message_user_account_9d71759a_fk_person_id; Type: FK CONSTRAINT; Schema: public; Owner: postgresAdmin
--

ALTER TABLE ONLY public.message
    ADD CONSTRAINT message_user_account_9d71759a_fk_person_id FOREIGN KEY (user_account) REFERENCES public.person(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgresAdmin
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;


--
-- PostgreSQL database dump complete
--

\unrestrict W0DoGhD6jOrvHLc01dyxWj0UM4ZyC2BK8T1dREaHKizfdHxzIrSQ0Rl3fllTGDa

--
-- Database "postgres" dump
--

--
-- PostgreSQL database dump
--

\restrict dKVeofzT1sZMBZ4vEEBGfYJvk5J9VBKtzS7Y2CGxu9pioBz9omXRq1wAPuEkvaI

-- Dumped from database version 16.14 (Debian 16.14-1.pgdg13+1)
-- Dumped by pg_dump version 16.14 (Debian 16.14-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE postgres;
--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: postgresAdmin
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE postgres OWNER TO "postgresAdmin";

\unrestrict dKVeofzT1sZMBZ4vEEBGfYJvk5J9VBKtzS7Y2CGxu9pioBz9omXRq1wAPuEkvaI
\connect postgres
\restrict dKVeofzT1sZMBZ4vEEBGfYJvk5J9VBKtzS7Y2CGxu9pioBz9omXRq1wAPuEkvaI

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: postgresAdmin
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- PostgreSQL database dump complete
--

\unrestrict dKVeofzT1sZMBZ4vEEBGfYJvk5J9VBKtzS7Y2CGxu9pioBz9omXRq1wAPuEkvaI

--
-- PostgreSQL database cluster dump complete
--

