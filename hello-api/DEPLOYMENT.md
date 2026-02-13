# Deployment Guide

## Local Server Deployment (Systemd)

API sudah di-deploy ke server local menggunakan **systemd service**.

### Service Details

- **Service Name**: `hello-api.service`
- **Port**: `8000`
- **Workers**: 2
- **Auto-start**: Enabled (starts on boot)
- **Auto-restart**: Enabled (restarts on failure)

### Service Management

**Start service:**
```bash
systemctl start hello-api
```

**Stop service:**
```bash
systemctl stop hello-api
```

**Restart service:**
```bash
systemctl restart hello-api
```

**Check status:**
```bash
systemctl status hello-api
```

**View logs:**
```bash
journalctl -u hello-api -f
```

### Testing the API

**Test root endpoint:**
```bash
curl http://localhost:8000/
```

**Test personalized greeting:**
```bash
curl "http://localhost:8000/greet?name=Faisol&lang=id"
```

**Test all greetings:**
```bash
curl http://localhost:8000/greetings
```

**Test health check:**
```bash
curl http://localhost:8000/health
```

### API Documentation

Interactive Swagger docs:
```
http://localhost:8000/docs
```

ReDoc documentation:
```
http://localhost:8000/redoc
```

### Server Info

- **Host**: 0.0.0.0 (all interfaces)
- **Port**: 8000
- **Workers**: 2 (for better performance)
- **User**: root
- **Working Directory**: /root/.openclaw/workspace/hello-api

### Updating the Application

After making code changes:

```bash
# Restart the service to apply changes
systemctl restart hello-api

# Or reload code without downtime (if using --reload flag)
systemctl reload hello-api
```

### Uninstall

To remove the service:

```bash
systemctl stop hello-api
systemctl disable hello-api
rm /etc/systemd/system/hello-api.service
systemctl daemon-reload
```

## Production Deployment (Nginx + Uvicorn)

For production with Nginx reverse proxy, see [NGINX-DEPLOYMENT.md](./NGINX-DEPLOYMENT.md) (coming soon).
