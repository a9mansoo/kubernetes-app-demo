## Repository Health:

[![Backend Stats](https://github.com/a9mansoo/kubernetes-deployment/actions/workflows/python-workflow.yml/badge.svg)](
https://github.com/a9mansoo/kubernetes-deployment/actions/workflows/python-workflow.yml
)
[![Frontend Stats](
https://github.com/a9mansoo/kubernetes-deployment/actions/workflows/react-workflow.yml/badge.svg
)](
https://github.com/a9mansoo/kubernetes-deployment/actions/workflows/react-workflow.yml
)
[![Image Stats](
https://github.com/a9mansoo/kubernetes-deployment/actions/workflows/build-project.yml/badge.svg
)](
https://github.com/a9mansoo/kubernetes-deployment/actions/workflows/build-project.yml
)

---

# Kubernetes Deployment Demo Platform

A production-style demo platform showcasing CI/CD automation, containerized applications, Kubernetes deployments, and infrastructure-focused development workflows.

---

## Overview

This project demonstrates how modern applications are built, validated, packaged, and deployed using DevOps practices commonly used in production environments.

The repository contains:

* A containerized FastAPI backend
* A React frontend
* GitHub Actions CI/CD pipelines
* Docker image build and publishing workflows
* Kubernetes manifests managed with Kustomize
* Automated release generation
* Environment separation for development and production deployments

The goal is not application complexity — it is to demonstrate **real-world delivery and deployment engineering practices**.

---

# Architecture

```text
┌──────────────────────┐
│     React Frontend   │
│  (NodePort Service)  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   FastAPI Backend    │
│  (ClusterIP Service) │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Kubernetes Cluster   │
│     (Minikube)       │
└──────────────────────┘
```

---

# Repository Structure

```text
.
├── backend/
├── frontend/
├── docker/
├── k8s/
│   ├── app/
│   ├── environments/
│   │   ├── dev/
│   │   └── prod/
├── .github/
│   └── workflows/
└── README.md
```

---

# Features

## CI/CD Pipelines

This project includes multiple GitHub Actions workflows:

* reusable Docker build workflow
* backend validation workflow
  * formatting validation (`black`)
  * linting (`ruff`)
  * automated tests (`pytest`)
  * Python code coverage reporting
* frontend React validation workflow
  * dependency installation
  * frontend build validation
  * linting and static analysis
* build + publish pipelines
* automated release generation
* concurrency-controlled workflows to prevent stale CI executions

---

## 🚀 Deployment Validation Workflow (Minikube Demo)

This is a **manually triggered production-style deployment validation pipeline** that runs a full Kubernetes deployment inside CI and validates it end-to-end.

---

### Trigger

* Manual execution via GitHub Actions
* Uses `workflow_dispatch`
* Runs under the `production` GitHub Environment

---

### 1. Ephemeral Cluster Setup

* Spins up a fresh Minikube cluster inside CI
* Ensures reproducible, isolated execution
* No external infrastructure dependencies

---

### 2. Namespace & Deployment

* Creates production namespace
* Applies Kubernetes manifests using Kustomize:

```text
k8s/environments/prod
```

* Deploys:

  * backend (FastAPI)
  * frontend (React)

---

### 3. Rollout Verification

* Waits for deployments to become healthy:

  * backend rollout
  * frontend rollout
* Fails fast on timeout
* Prints cluster state for debugging

---

### 4. Service Exposure

* Exposes frontend using Minikube service tunneling
* Resolves runtime-accessible URL inside CI

This ensures validation happens against a **real running system**, not just manifests.

---

### 5. End-to-End Smoke Test (Playwright)

A headless browser test validates the full stack:

* Launch Chromium in CI
* Navigate to frontend URL
* Wait for full network + rendering
* Capture screenshot (`ui.png`)

This validates:

* frontend rendering
* backend connectivity
* Kubernetes service routing
* internal DNS resolution

---

### 6. Artifact Capture

* Uploads UI screenshot as GitHub Actions artifact
* Provides visual proof of deployment success
* Enables debugging and auditability

---

### 7. Deployment Summary Report

Generates a CI summary including:

* Kubernetes rollout status
* service resolution status
* smoke test result
* overall pass/fail outcome
* artifact link (if available)

This acts as an **automated deployment report inside GitHub Actions UI**.

---

### Why This Matters

This workflow demonstrates production-grade deployment validation:

* ephemeral environments in CI
* Kubernetes rollout gating
* service-level validation
* real end-to-end testing (not mock tests)
* CI-based observability
* GitHub Environments control

---

### What Makes This Different

This pipeline proves:

* pods actually become healthy
* services are reachable
* frontend + backend integration works
* UI actually renders
* deployment is verifiably correct

---

# Backend Application

FastAPI service providing:

* health/readiness endpoints
* demo user API
* managed via `uv`

---

# Frontend Application

React application that:

* fetches backend data
* renders UI components
* demonstrates Kubernetes service communication

---

# Containerization

* Separate images for frontend and backend
* Built in CI pipelines
* Used for PR validation and release builds

---

# Kubernetes Deployment

Managed using Kustomize:

```text
k8s/environments/dev
k8s/environments/prod
```

### Resources:

* backend: ClusterIP service (internal only)
* frontend: NodePort service (external demo access)
* service-to-service communication via Kubernetes DNS

---

# DevOps Concepts Demonstrated

* GitHub Actions CI/CD pipelines
* reusable workflows
* Kubernetes deployments
* Kustomize environment separation
* ephemeral CI environments
* automated release pipelines
* PR validation gates
* end-to-end smoke testing
* deployment observability via artifacts
* GitHub Environments usage

---

# Local Development

## Requirements

* Docker
* Minikube
* kubectl
* Kustomize
* Node.js
* Python 3.12+
* uv

---

# Running Locally

## Backend

```bash
cd backend
uv sync
uv run fastapi dev
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

---

# Kubernetes Deployment

## Development

```bash
kubectl apply -k k8s/environments/dev
```

## Production

```bash
kubectl apply -k k8s/environments/prod
```

---

# Example CI/CD Flow

```text
PR opened
  ↓
CI validation (lint, tests, docker builds)
  ↓
Merge to main
  ↓
Tag release
  ↓
Build + publish images
  ↓
Optional: Minikube deployment validation workflow
  ↓
Artifacts + deployment report generated
```

---

# Why This Project Exists

Most demo repos stop at “it runs”.

This project focuses on:

* CI/CD correctness
* deployment verification
* environment consistency
* release automation
* real Kubernetes workflows
* observable delivery pipelines

---

# Future Improvements

* Helm charts
* GitOps with ArgoCD
* Prometheus + Grafana observability
* Canary deployments
* Terraform infrastructure provisioning
* ingress controller setup
* automated rollback on failure
* metrics-based deployment gates
