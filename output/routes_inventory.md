# AMP Route Inventory (Draft)

- Source: `/Users/edwardc/Projects/amp-backend/app.py`
- Route count: **128**

## Tag Counts
- `Admin / Ops`: 9
- `Agent Lifecycle`: 51
- `Analytics`: 7
- `Auth / Sessions`: 11
- `Dashboard`: 5
- `Frontend Shell`: 2
- `HITL`: 12
- `Internal`: 1
- `LLM Utilities`: 2
- `Log Proxy`: 4
- `Ops Utilities`: 3
- `Presence`: 1
- `RLHF`: 15
- `Uncategorized`: 2
- `User Profile`: 2
- `Workitems`: 4
- `Worktray`: 1

## Audience Counts
- `internal`: 3
- `partner`: 32
- `public`: 93

## Routes

| Path | Methods | Tags | Audience | Function | Line |
|---|---|---|---|---|---:|
| `/` | `GET` | `Frontend Shell` | `internal` | `spa_index` | 3660 |
| `/<path:path>` | `GET` | `Frontend Shell` | `internal` | `spa_index` | 3660 |
| `/api/abort` | `POST` | `Agent Lifecycle` | `public` | `abort_agent` | 8081 |
| `/api/admin/organizations` | `POST` | `Admin / Ops` | `partner` | `admin_create_organization` | 4228 |
| `/api/admin/organizations` | `GET` | `Admin / Ops` | `partner` | `admin_list_organizations` | 4180 |
| `/api/admin/organizations/<path:org_id>` | `DELETE` | `Admin / Ops` | `partner` | `admin_delete_organization` | 4367 |
| `/api/admin/organizations/<path:org_id>` | `PUT` | `Admin / Ops` | `partner` | `admin_update_organization` | 4289 |
| `/api/admin/presence` | `GET` | `Admin / Ops` | `partner` | `admin_presence_overview` | 3779 |
| `/api/admin/presence/chat` | `POST` | `Admin / Ops` | `partner` | `admin_presence_chat` | 3803 |
| `/api/admin/users` | `POST` | `Admin / Ops` | `partner` | `admin_create_user` | 3901 |
| `/api/admin/users` | `GET` | `Admin / Ops` | `partner` | `admin_list_users` | 4400 |
| `/api/admin/users/<path:target_username>` | `PUT` | `Admin / Ops` | `partner` | `admin_update_user` | 4446 |
| `/api/agent-tasks/complete` | `POST` | `Agent Lifecycle` | `public` | `complete_agent_task` | 5419 |
| `/api/agent-tasks/poll` | `GET` | `Agent Lifecycle` | `public` | `poll_agent_tasks` | 5363 |
| `/api/agent-tasks/register` | `POST` | `Agent Lifecycle` | `public` | `register_agent` | 5480 |
| `/api/agent-tasks/unregister` | `POST` | `Agent Lifecycle` | `public` | `unregister_remote_agent` | 5445 |
| `/api/agent/<agent_name>/autonomy_ops` | `GET` | `Agent Lifecycle` | `public` | `get_agent_autonomy_ops` | 11481 |
| `/api/agent/<agent_name>/autonomy_ops` | `POST` | `Agent Lifecycle` | `public` | `save_agent_autonomy_ops` | 11520 |
| `/api/agent/<agent_name>/criteria` | `GET` | `Agent Lifecycle` | `public` | `get_agent_criteria` | 11346 |
| `/api/agent/<agent_name>/criteria` | `POST` | `Agent Lifecycle` | `public` | `save_agent_criteria` | 11389 |
| `/api/agent/<agent_name>/eval-policy` | `POST` | `Agent Lifecycle` | `public` | `save_approve_eval_policy` | 11742 |
| `/api/agent/<agent_name>/eval-policy/deactivate` | `PUT` | `Agent Lifecycle` | `public` | `deactivate_eval_policy` | 14035 |
| `/api/agent/<agent_name>/eval-policy/reactivate` | `PUT` | `Agent Lifecycle` | `public` | `reactivate_eval_policy` | 14077 |
| `/api/agent/<agent_name>/features` | `GET` | `Agent Lifecycle` | `public` | `get_agent_features` | 11154 |
| `/api/agent/<agent_name>/features` | `POST` | `Agent Lifecycle` | `public` | `save_agent_features` | 11247 |
| `/api/agent/<agent_name>/features/generate-description` | `POST` | `Agent Lifecycle` | `public` | `generate_feature_description` | 11910 |
| `/api/agent/<agent_name>/policies/<version>` | `GET` | `Agent Lifecycle` | `public` | `get_policy_version` | 14007 |
| `/api/agent/<agent_name>/policies/current/rlhf_enabled` | `PUT` | `Agent Lifecycle` | `public` | `update_rlhf_enabled` | 14126 |
| `/api/agent/<agent_name>/policies/versions` | `GET` | `Agent Lifecycle` | `public` | `get_policy_versions` | 13934 |
| `/api/agent/<agent_name>/policy/approve` | `POST` | `Agent Lifecycle` | `public` | `approve_rlhf_policy` | 11595 |
| `/api/agent/init` | `POST` | `Agent Lifecycle` | `public` | `agent_init` | 10213 |
| `/api/agent/setState` | `POST` | `Agent Lifecycle` | `public` | `agent_set_state` | 10230 |
| `/api/agent/start` | `POST` | `Agent Lifecycle` | `public` | `agent_start` | 10219 |
| `/api/agents` | `GET` | `Agent Lifecycle` | `public` | `get_agents` | 4805 |
| `/api/agents/<instance_id>/llm_trace` | `GET` | `Agent Lifecycle` | `public` | `get_llm_trace` | 4974 |
| `/api/alp/agents` | `GET` | `Agent Lifecycle` | `public` | `alp_list_agents` | 9129 |
| `/api/alp/agents/<name>/defaults` | `GET` | `Agent Lifecycle` | `public` | `alp_get_defaults` | 9793 |
| `/api/alp/agents/<name>/defaults/artifacts` | `GET` | `Agent Lifecycle` | `public` | `alp_list_default_artifacts` | 9702 |
| `/api/alp/agents/<name>/defaults/artifacts/<path:filename>` | `GET` | `Agent Lifecycle` | `public` | `alp_get_default_artifact` | 9735 |
| `/api/alp/agents/<name>/defaults/config` | `POST` | `Agent Lifecycle` | `public` | `alp_update_defaults_config` | 9823 |
| `/api/alp/agents/<name>/defaults/prompt` | `POST` | `Agent Lifecycle` | `public` | `alp_update_defaults_prompt` | 9847 |
| `/api/alp/agents/<name>/instances` | `GET` | `Agent Lifecycle` | `public` | `alp_list_instances` | 9155 |
| `/api/alp/agents/<name>/instances/<instance_id>` | `DELETE` | `Agent Lifecycle` | `public` | `alp_delete_instance` | 9771 |
| `/api/alp/agents/<name>/instances/<instance_id>` | `GET` | `Agent Lifecycle` | `public` | `alp_get_instance` | 9490 |
| `/api/alp/agents/<name>/instances/<instance_id>/abort` | `POST` | `Agent Lifecycle` | `public` | `alp_abort_instance` | 13797 |
| `/api/alp/agents/<name>/instances/<instance_id>/artifacts` | `GET` | `Agent Lifecycle` | `public` | `alp_list_artifacts` | 9654 |
| `/api/alp/agents/<name>/instances/<instance_id>/artifacts/<filename>` | `POST` | `Agent Lifecycle` | `public` | `upload_artifact` | 10571 |
| `/api/alp/agents/<name>/instances/<instance_id>/artifacts/<path:filename>` | `GET` | `Agent Lifecycle` | `public` | `alp_get_artifact` | 9752 |
| `/api/alp/agents/<name>/instances/<instance_id>/chat` | `DELETE, GET, POST` | `Agent Lifecycle` | `public` | `alp_instance_chat` | 9552 |
| `/api/alp/agents/<name>/instances/<instance_id>/config` | `POST` | `Agent Lifecycle` | `public` | `alp_update_instance_config` | 10385 |
| `/api/alp/agents/<name>/instances/<instance_id>/execute` | `POST` | `Agent Lifecycle` | `public` | `alp_execute_instance` | 11149 |
| `/api/alp/agents/<name>/instances/<instance_id>/files` | `GET` | `Agent Lifecycle` | `public` | `get_instance_files` | 10437 |
| `/api/alp/agents/<name>/instances/<instance_id>/hitl-callback` | `POST` | `Agent Lifecycle` | `public` | `hitl_callback_remote_legacy` | 6492 |
| `/api/alp/agents/<name>/instances/<instance_id>/launch` | `POST` | `Agent Lifecycle` | `public` | `alp_launch_instance` | 10605 |
| `/api/alp/agents/<name>/instances/<instance_id>/log_initiated` | `POST` | `Agent Lifecycle` | `public` | `alp_log_initiated` | 10655 |
| `/api/alp/agents/<name>/instances/<instance_id>/meta` | `PUT` | `Agent Lifecycle` | `public` | `update_instance_meta` | 10475 |
| `/api/alp/agents/<name>/instances/<instance_id>/progress` | `POST` | `Agent Lifecycle` | `public` | `append_instance_progress` | 10532 |
| `/api/alp/agents/<name>/instances/<instance_id>/prompt` | `POST` | `Agent Lifecycle` | `public` | `alp_update_instance_prompt` | 10410 |
| `/api/alp/agents/<name>/instances/<instance_id>/summary` | `GET` | `Agent Lifecycle` | `public` | `alp_get_instance_summary` | 9453 |
| `/api/alp/agents/<name>/instances/<instance_id>/summary` | `POST` | `Agent Lifecycle` | `public` | `alp_save_instance_summary` | 9469 |
| `/api/alp/agents/<name>/runs` | `POST` | `Agent Lifecycle` | `public` | `alp_create_run` | 9871 |
| `/api/alp/agents/register-native` | `POST` | `Agent Lifecycle` | `public` | `register_native_agent` | 5522 |
| `/api/amp/chat` | `POST` | `Dashboard` | `partner` | `amp_chat_summary` | 5179 |
| `/api/amp/chat/history` | `DELETE, GET, POST` | `Dashboard` | `partner` | `amp_chat_history` | 5151 |
| `/api/amp/refresh-events` | `GET` | `Ops Utilities` | `partner` | `refresh_events` | 6502 |
| `/api/amp/sse-status` | `GET` | `Ops Utilities` | `partner` | `sse_status` | 6619 |
| `/api/amp/trigger-refresh` | `POST` | `Ops Utilities` | `partner` | `trigger_refresh` | 6609 |
| `/api/analytics/agent_events` | `GET` | `Analytics` | `public` | `analytics_agent_events` | 8577 |
| `/api/analytics/config` | `GET` | `Analytics` | `public` | `analytics_config` | 8495 |
| `/api/analytics/hitl_events` | `GET` | `Analytics` | `public` | `analytics_hitl_events` | 8626 |
| `/api/analytics/page_view` | `POST` | `Analytics` | `public` | `analytics_page_view` | 8504 |
| `/api/analytics/rlhf_autonomy` | `GET` | `Analytics` | `public` | `analytics_rlhf_autonomy` | 8716 |
| `/api/analytics/rlhf_stages` | `GET` | `Analytics` | `public` | `analytics_rlhf_stages` | 8778 |
| `/api/analytics/user_activity` | `GET` | `Analytics` | `public` | `analytics_user_activity` | 8673 |
| `/api/classify_intent` | `POST` | `LLM Utilities` | `partner` | `classify_intent_api` | 13890 |
| `/api/config` | `GET` | `Auth / Sessions` | `public` | `get_config` | 5324 |
| `/api/dashboard/chat` | `POST` | `Dashboard` | `partner` | `dashboard_chat` | 8320 |
| `/api/dashboard/chat/history` | `GET` | `Dashboard` | `partner` | `dashboard_chat_history` | 8482 |
| `/api/dashboard/demo-data/<path:filename>` | `GET` | `Dashboard` | `partner` | `dashboard_demo_data` | 8823 |
| `/api/hitl-agent` | `POST` | `HITL` | `public` | `proxy_hitl` | 5766 |
| `/api/hitl-agent/progress` | `GET` | `HITL` | `public` | `proxy_hitl_progress` | 5980 |
| `/api/hitl-agent/status` | `GET` | `HITL` | `public` | `proxy_hitl_status` | 5966 |
| `/api/hitl/agents/<name>/instances/<instance_id>/callback` | `POST` | `HITL` | `public` | `hitl_callback_remote` | 6486 |
| `/api/hitl/get-decision` | `GET` | `HITL` | `public` | `hitl_get_decision` | 6057 |
| `/api/hitl/progress` | `GET` | `HITL` | `public` | `proxy_hitl_progress` | 5980 |
| `/api/hitl/request` | `POST` | `HITL` | `public` | `proxy_hitl` | 5766 |
| `/api/hitl/status` | `GET` | `HITL` | `public` | `proxy_hitl_status` | 5966 |
| `/api/internal/users/resolve` | `POST` | `Internal` | `internal` | `resolve_user_identity` | 12200 |
| `/api/llm/classify` | `POST` | `LLM Utilities` | `partner` | `classify_llm_prompt` | 13901 |
| `/api/log` | `POST` | `Log Proxy` | `public` | `proxy_log` | 6338 |
| `/api/log/hitl-progress` | `GET` | `Log Proxy` | `public` | `proxy_log_hitl_progress` | 6411 |
| `/api/log/progress-all` | `GET` | `Log Proxy` | `public` | `proxy_log_progress_all` | 6394 |
| `/api/log_llm` | `POST` | `Log Proxy` | `public` | `log_llm_response` | 4786 |
| `/api/login` | `POST` | `Auth / Sessions` | `public` | `login` | 3680 |
| `/api/logout` | `POST` | `Auth / Sessions` | `public` | `logout` | 3750 |
| `/api/password/change` | `POST` | `Auth / Sessions` | `public` | `change_password` | 3988 |
| `/api/password/setup` | `POST` | `Auth / Sessions` | `public` | `setup_password` | 4019 |
| `/api/policy/library` | `GET` | `Uncategorized` | `public` | `list_policy_library` | 11871 |
| `/api/policy/library/<folder_name>` | `GET` | `Uncategorized` | `public` | `get_policy_library_template` | 11890 |
| `/api/presence/ping` | `POST` | `Presence` | `partner` | `presence_ping` | 3762 |
| `/api/register` | `OPTIONS, POST` | `Auth / Sessions` | `public` | `register` | 13862 |
| `/api/rlhf/approval_request` | `GET` | `RLHF` | `public` | `rlhf_fetch_approval_request` | 12678 |
| `/api/rlhf/bootstrap` | `POST` | `RLHF` | `public` | `rlhf_bootstrap_agent` | 13531 |
| `/api/rlhf/contract/approve` | `POST` | `RLHF` | `public` | `rlhf_approve_contract` | 12115 |
| `/api/rlhf/decision/bind_workitem` | `POST` | `RLHF` | `public` | `rlhf_bind_workitem` | 12322 |
| `/api/rlhf/decision_status` | `GET` | `RLHF` | `public` | `rlhf_decision_status` | 12779 |
| `/api/rlhf/jobs/enqueue` | `POST` | `RLHF` | `partner` | `rlhf_enqueue_job` | 13593 |
| `/api/rlhf/models` | `GET` | `RLHF` | `public` | `rlhf_model_registry_list` | 14232 |
| `/api/rlhf/models/<int:model_id>/activate` | `POST` | `RLHF` | `public` | `rlhf_model_registry_activate` | 14290 |
| `/api/rlhf/models/<int:model_id>/retire` | `POST` | `RLHF` | `public` | `rlhf_model_registry_retire` | 14339 |
| `/api/rlhf/outcome` | `POST` | `RLHF` | `public` | `rlhf_submit_outcome` | 12541 |
| `/api/rlhf/policy` | `GET` | `RLHF` | `public` | `rlhf_get_policy` | 12013 |
| `/api/rlhf/policy/save` | `POST` | `RLHF` | `public` | `rlhf_save_policy` | 12077 |
| `/api/rlhf/stage_tick/trigger` | `POST` | `RLHF` | `partner` | `rlhf_trigger_stage_tick` | 13665 |
| `/api/rlhf/status` | `GET` | `RLHF` | `partner` | `rlhf_status` | 12853 |
| `/api/rlhf/test/reset` | `POST` | `RLHF` | `partner` | `rlhf_reset_test_state` | 13734 |
| `/api/settings/api-keys` | `POST` | `Auth / Sessions` | `partner` | `settings_create_api_key` | 10327 |
| `/api/settings/api-keys` | `GET` | `Auth / Sessions` | `partner` | `settings_list_api_keys` | 10318 |
| `/api/settings/api-keys/<key_id>` | `DELETE` | `Auth / Sessions` | `partner` | `settings_revoke_api_key_by_id` | 10351 |
| `/api/settings/api-keys/<key_id>` | `PATCH` | `Auth / Sessions` | `partner` | `settings_update_api_key_label` | 10339 |
| `/api/settings/api-keys/<key_id>/reveal` | `GET` | `Auth / Sessions` | `partner` | `settings_reveal_api_key` | 10361 |
| `/api/user/profile` | `GET` | `User Profile` | `partner` | `get_user_profile` | 4098 |
| `/api/user/profile` | `PUT` | `User Profile` | `partner` | `update_user_profile` | 4142 |
| `/api/workitems` | `POST` | `Workitems, HITL` | `public` | `create_workitem` | 6969 |
| `/api/workitems` | `GET` | `Workitems, HITL` | `public` | `get_workitems` | 6631 |
| `/api/workitems/<workitem_id>` | `DELETE` | `Workitems, HITL` | `public` | `delete_workitem` | 7933 |
| `/api/workitems/<workitem_id>/status` | `PUT` | `Workitems, HITL` | `public` | `update_workitem_status` | 7730 |
| `/api/worktray/chat` | `POST` | `Worktray` | `partner` | `worktray_chat` | 7978 |
