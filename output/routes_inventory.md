# AMP Route Inventory (Draft)

- Source: `/Users/edwardc/Projects/amp-backend/app.py`
- Route count: **111**

## Tag Counts
- `Admin / Ops`: 6
- `Agent Lifecycle`: 48
- `Analytics`: 7
- `Auth / Sessions`: 9
- `Dashboard`: 5
- `Frontend Shell`: 2
- `HITL`: 5
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
- `partner`: 27
- `public`: 81

## Routes

| Path | Methods | Tags | Audience | Function | Line |
|---|---|---|---|---|---:|
| `/` | `GET` | `Frontend Shell` | `internal` | `spa_index` | 3104 |
| `/<path:path>` | `GET` | `Frontend Shell` | `internal` | `spa_index` | 3104 |
| `/api/abort` | `POST` | `Agent Lifecycle` | `public` | `abort_agent` | 6675 |
| `/api/admin/organizations` | `GET` | `Admin / Ops` | `partner` | `admin_list_organizations` | 3581 |
| `/api/admin/presence` | `GET` | `Admin / Ops` | `partner` | `admin_presence_overview` | 3223 |
| `/api/admin/presence/chat` | `POST` | `Admin / Ops` | `partner` | `admin_presence_chat` | 3247 |
| `/api/admin/users` | `POST` | `Admin / Ops` | `partner` | `admin_create_user` | 3345 |
| `/api/admin/users` | `GET` | `Admin / Ops` | `partner` | `admin_list_users` | 3604 |
| `/api/admin/users/<path:target_username>` | `PUT` | `Admin / Ops` | `partner` | `admin_update_user` | 3635 |
| `/api/agent-tasks/complete` | `POST` | `Agent Lifecycle` | `public` | `complete_agent_task` | 4588 |
| `/api/agent-tasks/poll` | `GET` | `Agent Lifecycle` | `public` | `poll_agent_tasks` | 4533 |
| `/api/agent-tasks/register` | `POST` | `Agent Lifecycle` | `public` | `register_agent` | 4649 |
| `/api/agent-tasks/unregister` | `POST` | `Agent Lifecycle` | `public` | `unregister_remote_agent` | 4614 |
| `/api/agent/<agent_name>/autonomy_ops` | `GET` | `Agent Lifecycle` | `public` | `get_agent_autonomy_ops` | 9694 |
| `/api/agent/<agent_name>/autonomy_ops` | `POST` | `Agent Lifecycle` | `public` | `save_agent_autonomy_ops` | 9733 |
| `/api/agent/<agent_name>/criteria` | `GET` | `Agent Lifecycle` | `public` | `get_agent_criteria` | 9559 |
| `/api/agent/<agent_name>/criteria` | `POST` | `Agent Lifecycle` | `public` | `save_agent_criteria` | 9602 |
| `/api/agent/<agent_name>/features` | `GET` | `Agent Lifecycle` | `public` | `get_agent_features` | 9376 |
| `/api/agent/<agent_name>/features` | `POST` | `Agent Lifecycle` | `public` | `save_agent_features` | 9466 |
| `/api/agent/<agent_name>/features/generate-description` | `POST` | `Agent Lifecycle` | `public` | `generate_feature_description` | 9955 |
| `/api/agent/<agent_name>/policies/<version>` | `GET` | `Agent Lifecycle` | `public` | `get_policy_version` | 11833 |
| `/api/agent/<agent_name>/policies/current/rlhf_enabled` | `PUT` | `Agent Lifecycle` | `public` | `update_rlhf_enabled` | 11861 |
| `/api/agent/<agent_name>/policies/versions` | `GET` | `Agent Lifecycle` | `public` | `get_policy_versions` | 11781 |
| `/api/agent/<agent_name>/policy/approve` | `POST` | `Agent Lifecycle` | `public` | `approve_rlhf_policy` | 9808 |
| `/api/agent/start` | `POST` | `Agent Lifecycle` | `public` | `agent_start` | 8585 |
| `/api/agents` | `GET` | `Agent Lifecycle` | `public` | `get_agents` | 3978 |
| `/api/agents/<instance_id>/llm_trace` | `GET` | `Agent Lifecycle` | `public` | `get_llm_trace` | 4144 |
| `/api/alp/agents` | `GET` | `Agent Lifecycle` | `public` | `alp_list_agents` | 7640 |
| `/api/alp/agents/<name>/defaults` | `GET` | `Agent Lifecycle` | `public` | `alp_get_defaults` | 8304 |
| `/api/alp/agents/<name>/defaults/artifacts` | `GET` | `Agent Lifecycle` | `public` | `alp_list_default_artifacts` | 8213 |
| `/api/alp/agents/<name>/defaults/artifacts/<path:filename>` | `GET` | `Agent Lifecycle` | `public` | `alp_get_default_artifact` | 8246 |
| `/api/alp/agents/<name>/defaults/config` | `POST` | `Agent Lifecycle` | `public` | `alp_update_defaults_config` | 8334 |
| `/api/alp/agents/<name>/defaults/prompt` | `POST` | `Agent Lifecycle` | `public` | `alp_update_defaults_prompt` | 8358 |
| `/api/alp/agents/<name>/instances` | `GET` | `Agent Lifecycle` | `public` | `alp_list_instances` | 7666 |
| `/api/alp/agents/<name>/instances/<instance_id>` | `DELETE` | `Agent Lifecycle` | `public` | `alp_delete_instance` | 8282 |
| `/api/alp/agents/<name>/instances/<instance_id>` | `GET` | `Agent Lifecycle` | `public` | `alp_get_instance` | 8001 |
| `/api/alp/agents/<name>/instances/<instance_id>/abort` | `POST` | `Agent Lifecycle` | `public` | `alp_abort_instance` | 11638 |
| `/api/alp/agents/<name>/instances/<instance_id>/artifacts` | `GET` | `Agent Lifecycle` | `public` | `alp_list_artifacts` | 8165 |
| `/api/alp/agents/<name>/instances/<instance_id>/artifacts/<filename>` | `POST` | `Agent Lifecycle` | `public` | `upload_artifact` | 8871 |
| `/api/alp/agents/<name>/instances/<instance_id>/artifacts/<path:filename>` | `GET` | `Agent Lifecycle` | `public` | `alp_get_artifact` | 8263 |
| `/api/alp/agents/<name>/instances/<instance_id>/chat` | `DELETE, GET, POST` | `Agent Lifecycle` | `public` | `alp_instance_chat` | 8063 |
| `/api/alp/agents/<name>/instances/<instance_id>/config` | `POST` | `Agent Lifecycle` | `public` | `alp_update_instance_config` | 8711 |
| `/api/alp/agents/<name>/instances/<instance_id>/execute` | `POST` | `Agent Lifecycle` | `public` | `alp_execute_instance` | 9365 |
| `/api/alp/agents/<name>/instances/<instance_id>/files` | `GET` | `Agent Lifecycle` | `public` | `get_instance_files` | 8763 |
| `/api/alp/agents/<name>/instances/<instance_id>/hitl-callback` | `POST` | `Agent Lifecycle` | `public` | `alp_hitl_callback` | 9370 |
| `/api/alp/agents/<name>/instances/<instance_id>/hitl-callback` | `POST` | `Agent Lifecycle` | `public` | `hitl_callback_remote` | 5082 |
| `/api/alp/agents/<name>/instances/<instance_id>/launch` | `POST` | `Agent Lifecycle` | `public` | `alp_launch_instance` | 8905 |
| `/api/alp/agents/<name>/instances/<instance_id>/log_initiated` | `POST` | `Agent Lifecycle` | `public` | `alp_log_initiated` | 8980 |
| `/api/alp/agents/<name>/instances/<instance_id>/meta` | `PUT` | `Agent Lifecycle` | `public` | `update_instance_meta` | 8801 |
| `/api/alp/agents/<name>/instances/<instance_id>/progress` | `POST` | `Agent Lifecycle` | `public` | `append_instance_progress` | 8832 |
| `/api/alp/agents/<name>/instances/<instance_id>/prompt` | `POST` | `Agent Lifecycle` | `public` | `alp_update_instance_prompt` | 8736 |
| `/api/alp/agents/<name>/instances/<instance_id>/summary` | `GET` | `Agent Lifecycle` | `public` | `alp_get_instance_summary` | 7964 |
| `/api/alp/agents/<name>/instances/<instance_id>/summary` | `POST` | `Agent Lifecycle` | `public` | `alp_save_instance_summary` | 7980 |
| `/api/alp/agents/<name>/runs` | `POST` | `Agent Lifecycle` | `public` | `alp_create_run` | 8382 |
| `/api/alp/agents/register-native` | `POST` | `Agent Lifecycle` | `public` | `register_native_agent` | 4688 |
| `/api/amp/chat` | `POST` | `Dashboard` | `partner` | `amp_chat_summary` | 4349 |
| `/api/amp/chat/history` | `DELETE, GET, POST` | `Dashboard` | `partner` | `amp_chat_history` | 4321 |
| `/api/amp/refresh-events` | `GET` | `Ops Utilities` | `partner` | `refresh_events` | 5179 |
| `/api/amp/sse-status` | `GET` | `Ops Utilities` | `partner` | `sse_status` | 5296 |
| `/api/amp/trigger-refresh` | `POST` | `Ops Utilities` | `partner` | `trigger_refresh` | 5286 |
| `/api/analytics/agent_events` | `GET` | `Analytics` | `public` | `analytics_agent_events` | 7171 |
| `/api/analytics/config` | `GET` | `Analytics` | `public` | `analytics_config` | 7089 |
| `/api/analytics/hitl_events` | `GET` | `Analytics` | `public` | `analytics_hitl_events` | 7220 |
| `/api/analytics/page_view` | `POST` | `Analytics` | `public` | `analytics_page_view` | 7098 |
| `/api/analytics/rlhf_autonomy` | `GET` | `Analytics` | `public` | `analytics_rlhf_autonomy` | 7310 |
| `/api/analytics/rlhf_stages` | `GET` | `Analytics` | `public` | `analytics_rlhf_stages` | 7372 |
| `/api/analytics/user_activity` | `GET` | `Analytics` | `public` | `analytics_user_activity` | 7267 |
| `/api/classify_intent` | `POST` | `LLM Utilities` | `partner` | `classify_intent_api` | 11737 |
| `/api/config` | `GET` | `Auth / Sessions` | `public` | `get_config` | 4494 |
| `/api/dashboard/chat` | `POST` | `Dashboard` | `partner` | `dashboard_chat` | 6914 |
| `/api/dashboard/chat/history` | `GET` | `Dashboard` | `partner` | `dashboard_chat_history` | 7076 |
| `/api/dashboard/demo-data/<path:filename>` | `GET` | `Dashboard` | `partner` | `dashboard_demo_data` | 7417 |
| `/api/hitl-agent` | `POST` | `HITL` | `public` | `proxy_hitl` | 4779 |
| `/api/init_agent` | `POST` | `Agent Lifecycle` | `public` | `init_agent` | 6666 |
| `/api/internal/users/resolve` | `POST` | `Internal` | `internal` | `resolve_user_identity` | 10245 |
| `/api/llm/classify` | `POST` | `LLM Utilities` | `partner` | `classify_llm_prompt` | 11748 |
| `/api/log` | `POST` | `Log Proxy` | `public` | `proxy_log` | 4990 |
| `/api/log/hitl-progress` | `GET` | `Log Proxy` | `public` | `proxy_log_hitl_progress` | 5063 |
| `/api/log/progress-all` | `GET` | `Log Proxy` | `public` | `proxy_log_progress_all` | 5046 |
| `/api/log_llm` | `POST` | `Log Proxy` | `public` | `log_llm_response` | 3959 |
| `/api/login` | `POST` | `Auth / Sessions` | `public` | `login` | 3124 |
| `/api/logout` | `POST` | `Auth / Sessions` | `public` | `logout` | 3194 |
| `/api/password/change` | `POST` | `Auth / Sessions` | `public` | `change_password` | 3433 |
| `/api/password/setup` | `POST` | `Auth / Sessions` | `public` | `setup_password` | 3464 |
| `/api/presence/ping` | `POST` | `Presence` | `partner` | `presence_ping` | 3206 |
| `/api/register` | `OPTIONS, POST` | `Auth / Sessions` | `public` | `register` | 11709 |
| `/api/rlhf/approval_request` | `GET` | `RLHF` | `public` | `rlhf_fetch_approval_request` | 10559 |
| `/api/rlhf/bootstrap` | `POST` | `RLHF` | `public` | `rlhf_bootstrap_agent` | 11372 |
| `/api/rlhf/contract/approve` | `POST` | `RLHF` | `public` | `rlhf_approve_contract` | 10160 |
| `/api/rlhf/decision/bind_workitem` | `POST` | `RLHF` | `public` | `rlhf_bind_workitem` | 10293 |
| `/api/rlhf/decision_status` | `GET` | `RLHF` | `public` | `rlhf_decision_status` | 10660 |
| `/api/rlhf/jobs/enqueue` | `POST` | `RLHF` | `partner` | `rlhf_enqueue_job` | 11434 |
| `/api/rlhf/models` | `GET` | `RLHF` | `public` | `rlhf_model_registry_list` | 11967 |
| `/api/rlhf/models/<int:model_id>/activate` | `POST` | `RLHF` | `public` | `rlhf_model_registry_activate` | 12025 |
| `/api/rlhf/models/<int:model_id>/retire` | `POST` | `RLHF` | `public` | `rlhf_model_registry_retire` | 12074 |
| `/api/rlhf/outcome` | `POST` | `RLHF` | `public` | `rlhf_submit_outcome` | 10422 |
| `/api/rlhf/policy` | `GET` | `RLHF` | `public` | `rlhf_get_policy` | 10058 |
| `/api/rlhf/policy/save` | `POST` | `RLHF` | `public` | `rlhf_save_policy` | 10122 |
| `/api/rlhf/stage_tick/trigger` | `POST` | `RLHF` | `partner` | `rlhf_trigger_stage_tick` | 11506 |
| `/api/rlhf/status` | `GET` | `RLHF` | `partner` | `rlhf_status` | 10734 |
| `/api/rlhf/test/reset` | `POST` | `RLHF` | `partner` | `rlhf_reset_test_state` | 11575 |
| `/api/settings/api-key` | `POST` | `Auth / Sessions` | `partner` | `settings_generate_api_key` | 8673 |
| `/api/settings/api-key` | `GET` | `Auth / Sessions` | `partner` | `settings_get_api_key` | 8684 |
| `/api/settings/api-key` | `DELETE` | `Auth / Sessions` | `partner` | `settings_revoke_api_key` | 8695 |
| `/api/user/profile` | `GET` | `User Profile` | `partner` | `get_user_profile` | 3529 |
| `/api/user/profile` | `PUT` | `User Profile` | `partner` | `update_user_profile` | 3552 |
| `/api/workitems` | `POST` | `Workitems, HITL` | `public` | `create_workitem` | 5646 |
| `/api/workitems` | `GET` | `Workitems, HITL` | `public` | `get_workitems` | 5308 |
| `/api/workitems/<workitem_id>` | `DELETE` | `Workitems, HITL` | `public` | `delete_workitem` | 6518 |
| `/api/workitems/<workitem_id>/status` | `PUT` | `Workitems, HITL` | `public` | `update_workitem_status` | 6371 |
| `/api/worktray/chat` | `POST` | `Worktray` | `partner` | `worktray_chat` | 6563 |
