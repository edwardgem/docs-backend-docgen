# AMP Route Inventory (Draft)

- Source: `/Users/edwardc/Projects/amp-backend/app.py`
- Route count: **121**

## Tag Counts
- `Admin / Ops`: 9
- `Agent Lifecycle`: 49
- `Analytics`: 7
- `Auth / Sessions`: 9
- `Dashboard`: 5
- `Frontend Shell`: 2
- `HITL`: 11
- `Internal`: 1
- `LLM Utilities`: 2
- `Log Proxy`: 4
- `Ops Utilities`: 3
- `Presence`: 1
- `RLHF`: 15
- `User Profile`: 2
- `Workitems`: 4
- `Worktray`: 1

## Audience Counts
- `internal`: 3
- `partner`: 30
- `public`: 88

## Routes

| Path | Methods | Tags | Audience | Function | Line |
|---|---|---|---|---|---:|
| `/` | `GET` | `Frontend Shell` | `internal` | `spa_index` | 3227 |
| `/<path:path>` | `GET` | `Frontend Shell` | `internal` | `spa_index` | 3227 |
| `/api/abort` | `POST` | `Agent Lifecycle` | `public` | `abort_agent` | 7519 |
| `/api/admin/organizations` | `POST` | `Admin / Ops` | `partner` | `admin_create_organization` | 3774 |
| `/api/admin/organizations` | `GET` | `Admin / Ops` | `partner` | `admin_list_organizations` | 3726 |
| `/api/admin/organizations/<path:org_id>` | `DELETE` | `Admin / Ops` | `partner` | `admin_delete_organization` | 3913 |
| `/api/admin/organizations/<path:org_id>` | `PUT` | `Admin / Ops` | `partner` | `admin_update_organization` | 3835 |
| `/api/admin/presence` | `GET` | `Admin / Ops` | `partner` | `admin_presence_overview` | 3346 |
| `/api/admin/presence/chat` | `POST` | `Admin / Ops` | `partner` | `admin_presence_chat` | 3370 |
| `/api/admin/users` | `POST` | `Admin / Ops` | `partner` | `admin_create_user` | 3468 |
| `/api/admin/users` | `GET` | `Admin / Ops` | `partner` | `admin_list_users` | 3946 |
| `/api/admin/users/<path:target_username>` | `PUT` | `Admin / Ops` | `partner` | `admin_update_user` | 3992 |
| `/api/agent-tasks/complete` | `POST` | `Agent Lifecycle` | `public` | `complete_agent_task` | 4964 |
| `/api/agent-tasks/poll` | `GET` | `Agent Lifecycle` | `public` | `poll_agent_tasks` | 4909 |
| `/api/agent-tasks/register` | `POST` | `Agent Lifecycle` | `public` | `register_agent` | 5025 |
| `/api/agent-tasks/unregister` | `POST` | `Agent Lifecycle` | `public` | `unregister_remote_agent` | 4990 |
| `/api/agent/<agent_name>/autonomy_ops` | `GET` | `Agent Lifecycle` | `public` | `get_agent_autonomy_ops` | 10728 |
| `/api/agent/<agent_name>/autonomy_ops` | `POST` | `Agent Lifecycle` | `public` | `save_agent_autonomy_ops` | 10767 |
| `/api/agent/<agent_name>/criteria` | `GET` | `Agent Lifecycle` | `public` | `get_agent_criteria` | 10593 |
| `/api/agent/<agent_name>/criteria` | `POST` | `Agent Lifecycle` | `public` | `save_agent_criteria` | 10636 |
| `/api/agent/<agent_name>/features` | `GET` | `Agent Lifecycle` | `public` | `get_agent_features` | 10410 |
| `/api/agent/<agent_name>/features` | `POST` | `Agent Lifecycle` | `public` | `save_agent_features` | 10500 |
| `/api/agent/<agent_name>/features/generate-description` | `POST` | `Agent Lifecycle` | `public` | `generate_feature_description` | 10989 |
| `/api/agent/<agent_name>/policies/<version>` | `GET` | `Agent Lifecycle` | `public` | `get_policy_version` | 13071 |
| `/api/agent/<agent_name>/policies/current/rlhf_enabled` | `PUT` | `Agent Lifecycle` | `public` | `update_rlhf_enabled` | 13099 |
| `/api/agent/<agent_name>/policies/versions` | `GET` | `Agent Lifecycle` | `public` | `get_policy_versions` | 13019 |
| `/api/agent/<agent_name>/policy/approve` | `POST` | `Agent Lifecycle` | `public` | `approve_rlhf_policy` | 10842 |
| `/api/agent/init` | `POST` | `Agent Lifecycle` | `public` | `agent_init` | 9567 |
| `/api/agent/setState` | `POST` | `Agent Lifecycle` | `public` | `agent_set_state` | 9584 |
| `/api/agent/start` | `POST` | `Agent Lifecycle` | `public` | `agent_start` | 9573 |
| `/api/agents` | `GET` | `Agent Lifecycle` | `public` | `get_agents` | 4351 |
| `/api/agents/<instance_id>/llm_trace` | `GET` | `Agent Lifecycle` | `public` | `get_llm_trace` | 4520 |
| `/api/alp/agents` | `GET` | `Agent Lifecycle` | `public` | `alp_list_agents` | 8484 |
| `/api/alp/agents/<name>/defaults` | `GET` | `Agent Lifecycle` | `public` | `alp_get_defaults` | 9148 |
| `/api/alp/agents/<name>/defaults/artifacts` | `GET` | `Agent Lifecycle` | `public` | `alp_list_default_artifacts` | 9057 |
| `/api/alp/agents/<name>/defaults/artifacts/<path:filename>` | `GET` | `Agent Lifecycle` | `public` | `alp_get_default_artifact` | 9090 |
| `/api/alp/agents/<name>/defaults/config` | `POST` | `Agent Lifecycle` | `public` | `alp_update_defaults_config` | 9178 |
| `/api/alp/agents/<name>/defaults/prompt` | `POST` | `Agent Lifecycle` | `public` | `alp_update_defaults_prompt` | 9202 |
| `/api/alp/agents/<name>/instances` | `GET` | `Agent Lifecycle` | `public` | `alp_list_instances` | 8510 |
| `/api/alp/agents/<name>/instances/<instance_id>` | `DELETE` | `Agent Lifecycle` | `public` | `alp_delete_instance` | 9126 |
| `/api/alp/agents/<name>/instances/<instance_id>` | `GET` | `Agent Lifecycle` | `public` | `alp_get_instance` | 8845 |
| `/api/alp/agents/<name>/instances/<instance_id>/abort` | `POST` | `Agent Lifecycle` | `public` | `alp_abort_instance` | 12876 |
| `/api/alp/agents/<name>/instances/<instance_id>/artifacts` | `GET` | `Agent Lifecycle` | `public` | `alp_list_artifacts` | 9009 |
| `/api/alp/agents/<name>/instances/<instance_id>/artifacts/<filename>` | `POST` | `Agent Lifecycle` | `public` | `upload_artifact` | 9896 |
| `/api/alp/agents/<name>/instances/<instance_id>/artifacts/<path:filename>` | `GET` | `Agent Lifecycle` | `public` | `alp_get_artifact` | 9107 |
| `/api/alp/agents/<name>/instances/<instance_id>/chat` | `DELETE, GET, POST` | `Agent Lifecycle` | `public` | `alp_instance_chat` | 8907 |
| `/api/alp/agents/<name>/instances/<instance_id>/config` | `POST` | `Agent Lifecycle` | `public` | `alp_update_instance_config` | 9710 |
| `/api/alp/agents/<name>/instances/<instance_id>/execute` | `POST` | `Agent Lifecycle` | `public` | `alp_execute_instance` | 10399 |
| `/api/alp/agents/<name>/instances/<instance_id>/files` | `GET` | `Agent Lifecycle` | `public` | `get_instance_files` | 9762 |
| `/api/alp/agents/<name>/instances/<instance_id>/hitl-callback` | `POST` | `Agent Lifecycle` | `public` | `alp_hitl_callback` | 10404 |
| `/api/alp/agents/<name>/instances/<instance_id>/hitl-callback` | `POST` | `Agent Lifecycle` | `public` | `hitl_callback_remote` | 5845 |
| `/api/alp/agents/<name>/instances/<instance_id>/launch` | `POST` | `Agent Lifecycle` | `public` | `alp_launch_instance` | 9930 |
| `/api/alp/agents/<name>/instances/<instance_id>/log_initiated` | `POST` | `Agent Lifecycle` | `public` | `alp_log_initiated` | 10005 |
| `/api/alp/agents/<name>/instances/<instance_id>/meta` | `PUT` | `Agent Lifecycle` | `public` | `update_instance_meta` | 9800 |
| `/api/alp/agents/<name>/instances/<instance_id>/progress` | `POST` | `Agent Lifecycle` | `public` | `append_instance_progress` | 9857 |
| `/api/alp/agents/<name>/instances/<instance_id>/prompt` | `POST` | `Agent Lifecycle` | `public` | `alp_update_instance_prompt` | 9735 |
| `/api/alp/agents/<name>/instances/<instance_id>/summary` | `GET` | `Agent Lifecycle` | `public` | `alp_get_instance_summary` | 8808 |
| `/api/alp/agents/<name>/instances/<instance_id>/summary` | `POST` | `Agent Lifecycle` | `public` | `alp_save_instance_summary` | 8824 |
| `/api/alp/agents/<name>/runs` | `POST` | `Agent Lifecycle` | `public` | `alp_create_run` | 9226 |
| `/api/alp/agents/register-native` | `POST` | `Agent Lifecycle` | `public` | `register_native_agent` | 5067 |
| `/api/amp/chat` | `POST` | `Dashboard` | `partner` | `amp_chat_summary` | 4725 |
| `/api/amp/chat/history` | `DELETE, GET, POST` | `Dashboard` | `partner` | `amp_chat_history` | 4697 |
| `/api/amp/refresh-events` | `GET` | `Ops Utilities` | `partner` | `refresh_events` | 5942 |
| `/api/amp/sse-status` | `GET` | `Ops Utilities` | `partner` | `sse_status` | 6059 |
| `/api/amp/trigger-refresh` | `POST` | `Ops Utilities` | `partner` | `trigger_refresh` | 6049 |
| `/api/analytics/agent_events` | `GET` | `Analytics` | `public` | `analytics_agent_events` | 8015 |
| `/api/analytics/config` | `GET` | `Analytics` | `public` | `analytics_config` | 7933 |
| `/api/analytics/hitl_events` | `GET` | `Analytics` | `public` | `analytics_hitl_events` | 8064 |
| `/api/analytics/page_view` | `POST` | `Analytics` | `public` | `analytics_page_view` | 7942 |
| `/api/analytics/rlhf_autonomy` | `GET` | `Analytics` | `public` | `analytics_rlhf_autonomy` | 8154 |
| `/api/analytics/rlhf_stages` | `GET` | `Analytics` | `public` | `analytics_rlhf_stages` | 8216 |
| `/api/analytics/user_activity` | `GET` | `Analytics` | `public` | `analytics_user_activity` | 8111 |
| `/api/classify_intent` | `POST` | `LLM Utilities` | `partner` | `classify_intent_api` | 12975 |
| `/api/config` | `GET` | `Auth / Sessions` | `public` | `get_config` | 4870 |
| `/api/dashboard/chat` | `POST` | `Dashboard` | `partner` | `dashboard_chat` | 7758 |
| `/api/dashboard/chat/history` | `GET` | `Dashboard` | `partner` | `dashboard_chat_history` | 7920 |
| `/api/dashboard/demo-data/<path:filename>` | `GET` | `Dashboard` | `partner` | `dashboard_demo_data` | 8261 |
| `/api/hitl-agent` | `POST` | `HITL` | `public` | `proxy_hitl` | 5287 |
| `/api/hitl-agent/progress` | `GET` | `HITL` | `public` | `proxy_hitl_progress` | 5395 |
| `/api/hitl-agent/status` | `GET` | `HITL` | `public` | `proxy_hitl_status` | 5381 |
| `/api/hitl/get-decision` | `GET` | `HITL` | `public` | `hitl_get_decision` | 5472 |
| `/api/hitl/progress` | `GET` | `HITL` | `public` | `proxy_hitl_progress` | 5395 |
| `/api/hitl/request` | `POST` | `HITL` | `public` | `proxy_hitl` | 5287 |
| `/api/hitl/status` | `GET` | `HITL` | `public` | `proxy_hitl_status` | 5381 |
| `/api/internal/users/resolve` | `POST` | `Internal` | `internal` | `resolve_user_identity` | 11279 |
| `/api/llm/classify` | `POST` | `LLM Utilities` | `partner` | `classify_llm_prompt` | 12986 |
| `/api/log` | `POST` | `Log Proxy` | `public` | `proxy_log` | 5753 |
| `/api/log/hitl-progress` | `GET` | `Log Proxy` | `public` | `proxy_log_hitl_progress` | 5826 |
| `/api/log/progress-all` | `GET` | `Log Proxy` | `public` | `proxy_log_progress_all` | 5809 |
| `/api/log_llm` | `POST` | `Log Proxy` | `public` | `log_llm_response` | 4332 |
| `/api/login` | `POST` | `Auth / Sessions` | `public` | `login` | 3247 |
| `/api/logout` | `POST` | `Auth / Sessions` | `public` | `logout` | 3317 |
| `/api/password/change` | `POST` | `Auth / Sessions` | `public` | `change_password` | 3555 |
| `/api/password/setup` | `POST` | `Auth / Sessions` | `public` | `setup_password` | 3586 |
| `/api/presence/ping` | `POST` | `Presence` | `partner` | `presence_ping` | 3329 |
| `/api/register` | `OPTIONS, POST` | `Auth / Sessions` | `public` | `register` | 12947 |
| `/api/rlhf/approval_request` | `GET` | `RLHF` | `public` | `rlhf_fetch_approval_request` | 11757 |
| `/api/rlhf/bootstrap` | `POST` | `RLHF` | `public` | `rlhf_bootstrap_agent` | 12610 |
| `/api/rlhf/contract/approve` | `POST` | `RLHF` | `public` | `rlhf_approve_contract` | 11194 |
| `/api/rlhf/decision/bind_workitem` | `POST` | `RLHF` | `public` | `rlhf_bind_workitem` | 11401 |
| `/api/rlhf/decision_status` | `GET` | `RLHF` | `public` | `rlhf_decision_status` | 11858 |
| `/api/rlhf/jobs/enqueue` | `POST` | `RLHF` | `partner` | `rlhf_enqueue_job` | 12672 |
| `/api/rlhf/models` | `GET` | `RLHF` | `public` | `rlhf_model_registry_list` | 13205 |
| `/api/rlhf/models/<int:model_id>/activate` | `POST` | `RLHF` | `public` | `rlhf_model_registry_activate` | 13263 |
| `/api/rlhf/models/<int:model_id>/retire` | `POST` | `RLHF` | `public` | `rlhf_model_registry_retire` | 13312 |
| `/api/rlhf/outcome` | `POST` | `RLHF` | `public` | `rlhf_submit_outcome` | 11620 |
| `/api/rlhf/policy` | `GET` | `RLHF` | `public` | `rlhf_get_policy` | 11092 |
| `/api/rlhf/policy/save` | `POST` | `RLHF` | `public` | `rlhf_save_policy` | 11156 |
| `/api/rlhf/stage_tick/trigger` | `POST` | `RLHF` | `partner` | `rlhf_trigger_stage_tick` | 12744 |
| `/api/rlhf/status` | `GET` | `RLHF` | `partner` | `rlhf_status` | 11932 |
| `/api/rlhf/test/reset` | `POST` | `RLHF` | `partner` | `rlhf_reset_test_state` | 12813 |
| `/api/settings/api-key` | `POST` | `Auth / Sessions` | `partner` | `settings_generate_api_key` | 9672 |
| `/api/settings/api-key` | `GET` | `Auth / Sessions` | `partner` | `settings_get_api_key` | 9683 |
| `/api/settings/api-key` | `DELETE` | `Auth / Sessions` | `partner` | `settings_revoke_api_key` | 9694 |
| `/api/user/profile` | `GET` | `User Profile` | `partner` | `get_user_profile` | 3665 |
| `/api/user/profile` | `PUT` | `User Profile` | `partner` | `update_user_profile` | 3697 |
| `/api/workitems` | `POST` | `Workitems, HITL` | `public` | `create_workitem` | 6409 |
| `/api/workitems` | `GET` | `Workitems, HITL` | `public` | `get_workitems` | 6071 |
| `/api/workitems/<workitem_id>` | `DELETE` | `Workitems, HITL` | `public` | `delete_workitem` | 7371 |
| `/api/workitems/<workitem_id>/status` | `PUT` | `Workitems, HITL` | `public` | `update_workitem_status` | 7168 |
| `/api/worktray/chat` | `POST` | `Worktray` | `partner` | `worktray_chat` | 7416 |
