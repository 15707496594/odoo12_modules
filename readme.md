### odoo12模块

模块 | 描述
---|---
accounting_pdf_reports | 会计pdf报表
om_account_accountant | odoo12会计
om_account_asset | 资产
om_account_budget | 预算
web_listview_sticky_header | 列表视图固定标题行
web_responsive | web端、手机端自适应backend主题
account_extend | 会计拓展
queue_job、queue_job_cron | 队列任务

### docker-compose部署

```
version: '2'
services:
  db:
    image: postgres:10
    volumes:
      - /xxx/db_data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: xxx
      POSTGRES_PASSWORD: xxx
    restart: always
  server:
    image: odoo:12.0
    ports:
      - "8069:8069"
      - "8072:8072"
    volumes:
      - /xxx/odoo12_modules:/mnt/extra-addons
      - /xxx/data:/var/lib/odoo
      - /xxxx/odoo.conf:/etc/odoo/odoo.conf
    environment:
      ODOO_QUEUE_JOB_PORT: 8069
    links:
      - db:db
    restart: always
```

