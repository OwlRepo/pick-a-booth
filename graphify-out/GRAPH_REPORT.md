# Graph Report - .  (2026-10-13)

## Corpus Check
- 350 files · ~103,630 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2741 nodes · 5872 edges · 178 communities (151 shown, 27 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 333 edges (avg confidence: 0.61)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- DB Models & Alembic
- App Config & Acquisition Wiring
- resilientservice cluster
- Admin Files & Enumerate API
- Background Removal (rembg)
- Media Collection Service
- Service Container Lifecycle
- TDD Test Repo Fixture
- __init__ cluster
- Commander Plugin
- Image Processing Steps
- Image/Animation Benchmarks
- Wigglecam Backend
- Backend Mode Controller
- Processing Event Hooks
- Picamera2 Tests
- DB Models & Alembic
- Filter API
- Admin Auth (JWT)
- Picamera2 Backend
- Collage/Animation Merge
- AI Workflow Phase Docs
- Virtual Camera Source
- Acquisition Service
- Multicamera Steps
- AI Engineering Agents
- test_check_test_layers cluster
- Persona Generator
- DB Models & Alembic
- Gphoto2 Backend
- Abstract Camera Backend
- Encode Benchmarks
- Information Service
- Plugin Hookspecs & Stats
- PyAV Webcam Backend
- TDD Name Rules
- Config Admin Tests
- Actions Config Group
- Rclone Synchronizer
- AI Workflow Phase Docs
- TDD Lib & Bash Guard
- Persona Prompts
- Processing API
- Plugin Manager
- AI Workflow Phase Docs
- Media Pipeline Core
- digiCamControl Backend
- Configuration Service
- Media Pipeline Core
- AI Engineering Workflows
- Logging Service
- Share-on-Demand PHP
- Acquisition API
- Share Config Group
- Processing Service
- TDD Red CLI
- gpio cluster
- GPIO Pin Handling
- Acquisition API Tests
- Plugin Hookspecs & Stats
- simple cluster
- AI Runtime Rules & Templates
- filter_pilgram2 cluster
- baseconfig cluster
- Acquisition API
- repeatedtimer cluster
- Container, Schemas & SSE
- base cluster
- encode_animation_test cluster
- sse_ cluster
- tdd_gate cluster
- Share Config Group
- charuco_board cluster
- scale_image_test cluster
- stream_lores_test cluster
- test_system cluster
- Plugin Hookspecs & Stats
- Admin Auth (JWT)
- BaseService
- test_filter cluster
- multicamera cluster
- video cluster
- simple cluster
- Persona Prompts
- misc cluster
- crop_image_test cluster
- base cluster
- Plugin Hookspecs & Stats
- abstractbackend cluster
- share cluster
- printer cluster
- test_multicamera cluster
- misc cluster
- image cluster
- __init__ cluster
- Plugin Hookspecs & Stats
- Processing API
- media cluster
- resize_algorithm_test cluster
- BaseService
- Processing Event Hooks
- offset_image_test cluster
- scale_video_test cluster
- test_actions cluster
- AI Engineering Workflows
- project-memory cluster
- processing cluster
- tdd_red_guard cluster
- Abstract Camera Backend
- encode_video_test cluster
- AI Engineering Workflows
- multicamera cluster
- test_share cluster
- Plugin Hookspecs & Stats
- App Factory & Startup
- test_information cluster
- test_static cluster
- test_tdd_lib cluster
- App Factory & Startup
- misc cluster
- misc cluster
- gpio cluster
- gpio cluster
- filter_pilgram2_test cluster
- test_enumerate cluster
- tdd_lib cluster
- base_plugin cluster
- GPIO Lights Plugin
- test_debug cluster
- project-memory cluster
- Persona Prompts
- Image Processing Steps
- Persona Prompts
- AI Runtime Rules & Templates
- eod-report cluster
- project-memory cluster
- Image Processing Steps
- new-task-worktree cluster
- __init__ cluster
- __init__ cluster
- __init__ cluster
- AI Engineering Workflows
- Persona Prompts
- Persona Prompts
- Persona Prompts
- Persona Prompts
- CONTRIBUTING cluster
- pyproject cluster
- Persona Generator

## God Nodes (most connected - your core abstractions)
1. `Mediaitem` - 57 edges
2. `AcquisitionService` - 55 edges
3. `AbstractBackend` - 48 edges
4. `JobModelBase` - 47 edges
5. `MediacollectionService` - 44 edges
6. `make_repo()` - 43 edges
7. `BaseService` - 40 edges
8. `InformationService` - 36 edges
9. `BaseSession` - 33 edges
10. `ImageContext` - 32 edges

## Surprising Connections (you probably didn't know these)
- `Worktree and branch isolation` --semantically_similar_to--> `Task worktree isolation`  [INFERRED] [semantically similar]
  docs/ai/execution.md → AGENTS.md
- `Dispatch Round Structure` --semantically_similar_to--> `Contract-First Dispatch`  [INFERRED] [semantically similar]
  docs/ai/agent-orchestration.md → agents/src/prompts/project-manager.md
- `Dependency updates risk (no dependabot)` --conceptually_related_to--> `ADR-0003 Desktop app; own CI, no server deploy`  [INFERRED]
  docs/ai/risk-register.md → .ai-engineering/memory/architecture-decisions.md
- `Upstream sync risk` --conceptually_related_to--> `ADR-0003 Desktop app; own CI, no server deploy`  [INFERRED]
  docs/ai/risk-register.md → .ai-engineering/memory/architecture-decisions.md
- `test_edge_find_bash_write_targets_detects_writes()` --calls--> `find_bash_write_targets()`  [INFERRED]
  scripts/tests/test_tdd_lib.py → scripts/ci/tdd_lib.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **CI quality gate steps** — docs_plans_desktop_ci_test_layer_guard, docs_ai_testing_strategy_tdd_gate, docs_ai_testing_strategy_script_tests, docs_ai_testing_strategy_agents_lint, _github_workflows_ci_gate_job [EXTRACTED 1.00]
- **Replace upstream CI with own desktop CI** — docs_plans_desktop_ci_upstream_photobooth_app_ci, _ai_engineering_memory_architecture_decisions_adr_0003, _github_workflows_ci, docs_plans_desktop_ci_desktop_app_direction, docs_plans_desktop_ci_optra_quality_gate [EXTRACTED 1.00]
- **Strict TDD enforcement layers** — docs_ai_testing_strategy_strict_tdd, docs_ai_testing_strategy_tdd_red, docs_plans_desktop_ci_test_layer_guard, docs_ai_testing_strategy_tdd_gate, docs_ai_testing_strategy_waivers [INFERRED 0.85]
- **Canonical flow mandatory doc loads** — agents_canonical_task_flow, docs_ai_plan_template, docs_ai_execution, docs_ai_testing_strategy, docs_ai_autonomous_engineering [EXTRACTED 0.90]
- **Contract-first multi-agent dispatch** — agents_src_prompts_project_manager_contract_first_dispatch, docs_ai_agent_orchestration_dispatch_round_structure, docs_ai_agent_orchestration_file_ownership_rule, docs_ai_agent_orchestration_round_1b_red, docs_ai_agent_orchestration_round_4_qa_fan_out [INFERRED 0.85]
- **Agent role contracts** — ai_engineering_agents_product_manager, ai_engineering_agents_architect, ai_engineering_agents_coordinator, ai_engineering_agents_implementer, ai_engineering_agents_reviewer, ai_engineering_agents_qa, ai_engineering_agents_reporter [EXTRACTED 1.00]
- **Task lifecycle state docs** — ai_engineering_core_task_lifecycle, ai_engineering_core_task_state_machine, ai_engineering_core_task_state_machine_skipped_already_implemented, ai_engineering_core_task_state_machine_blocked_states, ai_engineering_core_task_state_machine_waiting_approval [INFERRED 0.85]
- **Report templates** — ai_engineering_templates_execution_report_doc, ai_engineering_templates_review_report_doc, ai_engineering_templates_qa_report_doc, ai_engineering_templates_pr_report_doc, ai_engineering_templates_eod_report_doc [INFERRED 0.75]
- **Phase-loaded AI workflow workflow docs** — _ai_engineering_workflows_task_intake, _ai_engineering_workflows_feature_development, _ai_engineering_workflows_review_process, _ai_engineering_workflows_release_process, _ai_engineering_workflows_bug_fix, _ai_engineering_workflows_blocker_handling, _ai_engineering_workflows_daily_cycle [INFERRED 0.85]
- **Canonical task flow phase docs** — docs_ai_planning, docs_ai_execution, docs_ai_handoff, docs_ai_task_router [EXTRACTED 0.95]
- **Plan prompt templates** — docs_ai_prompts_bugfix_rca, docs_ai_prompts_bugfix_plan, docs_ai_prompts_feature_plan, docs_ai_prompts_refactor_plan [EXTRACTED 0.90]

## Communities (178 total, 27 thin omitted)

### Community 0 - "DB Models & Alembic"
Cohesion: 0.05
Nodes (45): datetime, FastAPI, _create_app(), lifespan(), create_db_and_tables(), MediaitemPublic, BaseModel, ShareLimitsPublic (+37 more)

### Community 1 - "App Config & Acquisition Wiring"
Cohesion: 0.06
Nodes (34): AppConfig class providing central config, manage up to two photobooth-app backends in this module, AnimationConfigurationSet, BaseConfigurationSet, CollageConfigurationSet, GroupActions, MulticameraConfigurationSet, MulticameraJobControl (+26 more)

### Community 2 - "resilientservice cluster"
Cohesion: 0.05
Nodes (32): Common, BaseModel, WledConfig, Enum, Event, hookimpl, State, To start the resilient service (+24 more)

### Community 3 - "Admin Files & Enumerate API"
Cohesion: 0.05
Nodes (59): Body, api_get_rclone_remotes(), api_get_serial_ports(), api_get_usbcameras(), get_search(), get, api_clearrecycledir(), create_upload_file() (+51 more)

### Community 4 - "Background Removal (rembg)"
Cohesion: 0.06
Nodes (36): SessionOptions, naive_cutout(), Any, PILImage, The util is very much inspired by https://github.com/danielgatis/rembg Thank…, Remove the background from an input image., remove(), new_session() (+28 more)

### Community 5 - "Media Collection Service"
Cohesion: 0.05
Nodes (47): MediacollectionService, UUID, Handle all image related stuff, DbListenter, client(), client_authenticated(), global_function_setup1(), global_function_setup2() (+39 more)

### Community 6 - "Service Container Lifecycle"
Cohesion: 0.06
Nodes (41): DigitalOutputDevice, Events, Container, stop all services first (reverse order), then start them again., GpioLight, GpioLightsConfig, BaseModel, AppDigitalOutputDevice (+33 more)

### Community 7 - "TDD Test Repo Fixture"
Cohesion: 0.10
Nodes (50): git(), make_repo(), Path, Repo, run_script(), write(), cited_paths(), Path (+42 more)

### Community 8 - "__init__ cluster"
Cohesion: 0.06
Nodes (34): hookspec, PluginAcquisitionSpec, PluginManagementSpec, PluginMediacollectionSpec, PluginMediaprocessingSpec, PluginStatemachineSpec, Enum, Event (+26 more)

### Community 9 - "Commander Plugin"
Cohesion: 0.11
Nodes (31): eventHooks, field_validator, Commander, Event, hookimpl, MediaitemTypes, State, ThreadCommand (+23 more)

### Community 10 - "Image Processing Steps"
Cohesion: 0.12
Nodes (42): PluginFilters, TextsConfig, ImageContext, process_image_inner(), Unified handling of images that are just one single capture: 1pictaken…, FillBackgroundStep, get_plugin_avail_filters(), get_plugin_userselectable_filters() (+34 more)

### Community 11 - "Image/Animation Benchmarks"
Cohesion: 0.07
Nodes (34): BytesIO, benchmark, test_transpose_piexif(), test_transpose_pillow(), transpose_piexif(), transpose_pillow(), ffmpeg_hq_optimizedquality_scale(), ffmpeg_hq_optimizedspeed_scale() (+26 more)

### Community 12 - "Wigglecam Backend"
Cohesion: 0.08
Nodes (24): model_validator, MulticamRequest, Path, Trigger a capture request and collect hi-res images from all cameras., Background loop to receive lores frames., # TODO: get highres from the one camera selected, for now get all and return…, WigglecamBackend, BaseModelCamera (+16 more)

### Community 13 - "Backend Mode Controller"
Cohesion: 0.06
Nodes (20): Modes, https://photobooth-app.org/setup/configuration/qrshareservice/, LoresBroadcastRes, ModeController, ABC, Orientation, Path, # TODO: validate 0.5 tolerance. (+12 more)

### Community 14 - "Processing Event Hooks"
Cohesion: 0.06
Nodes (16): AnimationMergeDefinition, CollageMergeDefinition, BaseModel, JobModelBase, ABC, Event, Path, UUID (+8 more)

### Community 15 - "Picamera2 Tests"
Cohesion: 0.10
Nodes (20): Convert JPG/MJPG and YUVY pixelformat to output JPG, WebcamV4lBackend, GroupCameraV4l2, webcameras(), test_emulated_get_images_disable_liveview_recovery_more_retries(), backend_pyav(), fixture, get lores and hires images from backend and assert (+12 more)

### Community 16 - "DB Models & Alembic"
Cohesion: 0.08
Nodes (17): DeclarativeBase, listens_for, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Base, Cacheditem (+9 more)

### Community 17 - "Filter API"
Cohesion: 0.12
Nodes (28): api_get_calibration_stats(), api_get_result(), get, api_applyfilter(), api_get_preview_image_filtered(), api_get_userselectable_filters(), get, patch (+20 more)

### Community 18 - "Admin Auth (JWT)"
Cohesion: 0.12
Nodes (31): oauth2_scheme, OAuth2PasswordRequestForm, login_for_access_token(), Depends, get, post, read_users_me(), authenticate_user() (+23 more)

### Community 19 - "Picamera2 Backend"
Cohesion: 0.08
Nodes (14): Picamera2Backend, Path, Every camera tuning file usually has at least "normal", "short" and "long"…, picamera2 has local start_recording, which overrides the abstract class…, on start set autofocus to continuous if requested by config or auto and trigger…, GroupCameraPicamera2, is_rpi(), detect if computer is a raspberry pi (any model) Returns: bool: true is… (+6 more)

### Community 20 - "Collage/Animation Merge"
Cohesion: 0.13
Nodes (19): AnimationContext, CollageContext, AlignSizesStep, AddPredefinedImagesStep, PostPredefinedImagesStep, NextStep, captures are postprocessed during capture, predefined not. the mergedefinition…, NextStep (+11 more)

### Community 21 - "AI Workflow Phase Docs"
Cohesion: 0.08
Nodes (28): ADR-0001 AI engineering workflow port, ADR-0002 Claude Code only agent runtime, ADR-0003 Desktop app; own CI, no server deploy, CI job desktop-tests (OS matrix), CI job gate (Quality gate), One workflow only rule, pyproject.toml, Worktree per task flow (+20 more)

### Community 22 - "Virtual Camera Source"
Cohesion: 0.10
Nodes (11): FolderImageSource, Path, for other threads to receive a hq JPEG image, Read all JPEGs from a folder, mmap them once, and cycle endlessly., VirtualCameraBackend, backend_virtual(), fixture, get lores and hires images from backend and assert (+3 more)

### Community 23 - "Acquisition Service"
Cohesion: 0.09
Nodes (16): AcquisitionService, Path, called by job processor when a countdown for video is started, Gather stats from active backends. Backend stats are converted to dict to be…, called by job processor when a countdown for stills is started, _acqs(), fixture, get video from service (+8 more)

### Community 24 - "Multicamera Steps"
Cohesion: 0.12
Nodes (18): MatLike, MulticameraContext, AlignAsPerCalibrationStep, AutoPivotPointStep, CropCommonAreaStep, OffsetPerOpticalFlowStep, Image, NextStep (+10 more)

### Community 25 - "AI Engineering Agents"
Cohesion: 0.10
Nodes (28): architect, coordinator, implementer, product-manager, qa, reporter, reviewer, PILOT_FROZEN activation (+20 more)

### Community 26 - "test_check_test_layers cluster"
Cohesion: 0.15
Nodes (27): Exception, Reader, git(), _is_wiring_only(), main(), problems_for(), Require the tests for every layer a commit touches (CI: ci.yml, job `gate`). uv…, Missing-test messages for one commit's changed files. (+19 more)

### Community 27 - "Persona Generator"
Cohesion: 0.13
Nodes (24): Path, Persona, check(), claude_file(), compute_targets(), _escape(), find_duplicate_owned_globs(), generate() (+16 more)

### Community 28 - "DB Models & Alembic"
Cohesion: 0.10
Nodes (9): Mediaitem, Database, UUID, Files, delete all images, inclusive thumbnails, ..., SseEventDbInsert, _mediaitem(), start service and try to download an image (+1 more)

### Community 29 - "Gphoto2 Backend"
Cohesion: 0.12
Nodes (11): StillRequest, GpEvents, Gphoto2Backend, GpWidgets, Enum, Gphoto2Parameters, Configure different settings when switching between modes., backend_gphoto2() (+3 more)

### Community 30 - "Abstract Camera Backend"
Cohesion: 0.09
Nodes (12): AbstractBackend, BackendStats, Wird im stream-thread aufgerufen, wenn es passend für einen potentiellen mode-…, defines some common stats - if backend supports, they return these properties,…, called during device setup, called internally by supervising if liveview frames are requested, called externally via events and used to change to a preview mode if necessary, called externally via events and used to change to a capture mode if necessary (+4 more)

### Community 31 - "Encode Benchmarks"
Cohesion: 0.13
Nodes (22): cv2_encode_jpg(), cv2_encode_png_lossless(), cv2_encode_webp(), image(), image_hires(), image_lores(), library(), library_yuv420() (+14 more)

### Community 32 - "Information Service"
Cohesion: 0.13
Nodes (3): InformationService, Any, Raspberry Pi system health monitor using vcgencmd. Decode throttled bitmask…

### Community 33 - "Plugin Hookspecs & Stats"
Cohesion: 0.20
Nodes (11): PipelineStats, PrioritizedJob, ThreadedImmediateSyncPipeline, CopyOperation, DeleteOperation, JobResult, JobStatus, Enum (+3 more)

### Community 34 - "PyAV Webcam Backend"
Cohesion: 0.11
Nodes (7): InputContainer, Packet, WebcamPyavBackend, PermanentFault, Raised from within the services when the service should not attempt recovery., test_optimize_mode(), VideoStream

### Community 35 - "TDD Name Rules"
Cohesion: 0.15
Nodes (22): check_names(), extract_test_names(), judge_red(), parse_waivers(), added: names introduced by the diff (any file). new_files: full ordered names…, Test functions pytest would collect, in declaration order. Strings, comments…, added(), test_edge_extract_handles_async_methods_and_skips_fixtures() (+14 more)

### Community 36 - "Config Admin Tests"
Cohesion: 0.14
Nodes (19): AppConfig, AppConfig class glueing all together In the case where a value is specified for…, patch, TestClient, test_config_endpoints_ui(), test_config_getschema(), test_config_patch(), test_config_post_validationerror() (+11 more)

### Community 37 - "Actions Config Group"
Cohesion: 0.14
Nodes (10): SingleImageConfigurationSet, SingleImageJobControl, JobModelImage, Event, _acqs(), fixture, test_jobmodel_start_count(), test_jobmodel_start_count_bigger_offset() (+2 more)

### Community 38 - "Rclone Synchronizer"
Cohesion: 0.10
Nodes (12): RcloneApi, UUID, setup the resource right before run_service logic, tear down the resource right after run_service logic and in case of crashes, service logic to be run when the service is started, ShareOnDemandService, fixture, start service and try to download an image that does not exist (+4 more)

### Community 39 - "AI Workflow Phase Docs"
Cohesion: 0.14
Nodes (15): Canonical Task Flow, Graphify discovery, Task worktree isolation, Origin freshness and app-managed worktrees, Implementation rules, Mandatory Graphify closeout, QA mode, Review mode (+7 more)

### Community 40 - "TDD Lib & Bash Guard"
Cohesion: 0.13
Nodes (20): expr, find_bash_write_targets(), _is_fixture(), is_guarded_source(), _is_path_arg(), kind_of(), NamedTuple, Shared rules for the TDD gate (CI), `uv run poe tdd:red` (local) and the Claude… (+12 more)

### Community 41 - "Persona Prompts"
Cohesion: 0.11
Nodes (17): Automatic agent routing default, Contract-First Dispatch, project-manager persona, accessibility-auditor persona, code-reviewer persona, db-architect persona, Dispatch Round Structure, fastapi-backend-dev persona (+9 more)

### Community 42 - "Processing API"
Cohesion: 0.19
Nodes (18): BackgroundTasks, deprecated, api_cmd_abort_get(), api_cmd_confirm_get(), api_cmd_reject_get(), api_get_preview_image_filtered(), get, UUID (+10 more)

### Community 43 - "Plugin Manager"
Cohesion: 0.15
Nodes (7): BasePlugin, PluginManagerService, When the pluginmanager is started, it will start all registered plugins that…, When the pluginmanager is stoppped, it will stop all registered plugins that…, pluginmanager_service(), fixture, test_list_plugins()

### Community 44 - "AI Workflow Phase Docs"
Cohesion: 0.15
Nodes (8): Application layers (routers, services, backends, plugins, db), Unattended Alembic migrations at start, SQLite and Alembic data model, Maps are not proof; code wins, graphify-out/graph.json, Graphify discovery first, Migration rules, Task classification routing

### Community 45 - "Media Pipeline Core"
Cohesion: 0.17
Nodes (10): Context, ErrorHandler, _default_error_handler(), Pipeline, PipelineCursor, PipelineError, PipelineStep, Any (+2 more)

### Community 46 - "digiCamControl Backend"
Cohesion: 0.12
Nodes (7): HTTPServer, DigicamcontrolBackend, r""" Digicamcontrol backend implementation Quirks: - using webfrontend only…, GroupCameraDigicamcontrol, backend_digicamcontrol_emulated(), fixture, test_optimize_mode()

### Community 47 - "Configuration Service"
Cohesion: 0.18
Nodes (7): ConfigurationService, Any, AnyStr, configuration_service(), fixture, test_plugin_config_get_current(), test_plugin_config_get_schema()

### Community 48 - "Media Pipeline Core"
Cohesion: 0.22
Nodes (12): VideoContext, BoomerangStep, LoopStep, NextStep, benchmark, test_encode_boomerang_pyav(), test_loop_pyav(), video_boomerangPyav_stage() (+4 more)

### Community 49 - "AI Engineering Workflows"
Cohesion: 0.12
Nodes (16): Blocker Handling workflow, Task Intake workflow, Caveman ultra policy, Core principles, Strict TDD (principle 6b), Structured autonomous work orders, AI_WORKFLOW.md pointer, Round 1b RED (+8 more)

### Community 50 - "Logging Service"
Cohesion: 0.13
Nodes (7): ExceptHookArgs, LogRecord, ConsoleColorFormatter, EventstreamLogHandler, LoggingService, mute some logger by rasing their log level, Logging handler to emit events to eventstream; to be displayed in console.log…

### Community 51 - "Share-on-Demand PHP"
Cohesion: 0.22
Nodes (3): RuntimeException, AuthException, ShareService

### Community 52 - "Acquisition API"
Cohesion: 0.17
Nodes (15): api_trigger_model(), ActionType, get, api_download_item_id_get_sharelinks(), api_share_item_id(), api_share_latest(), get, post (+7 more)

### Community 53 - "Share Config Group"
Cohesion: 0.20
Nodes (17): BaseModel, Configure options to share or print images., Configure stages how to process mediaitem before printing on paper., ShareConfigurationSet, ShareProcessing, _container(), fixture, patch (+9 more)

### Community 54 - "Processing Service"
Cohesion: 0.16
Nodes (4): ProcessingService, ActionType, if queue is initialized on _external_cmd_queue, a user request is waited for., userEvents

### Community 55 - "TDD Red CLI"
Cohesion: 0.22
Nodes (15): changed_entries(), git(), main(), parse_args(), Exception, Path, `uv run poe tdd:red`: run this branch's changed tests BEFORE implementing and…, Committed + staged + unstaged changes against the merge-base, plus untracked… (+7 more)

### Community 56 - "gpio cluster"
Cohesion: 0.14
Nodes (7): GroupHardwareInputOutput, BaseModel, Configure hardware GPIO, keyboard and more. Find integration information in the…, GpioService, ActionType, gpio_service(), fixture

### Community 57 - "GPIO Pin Handling"
Cohesion: 0.22
Nodes (12): PinHandler, pinhandler1(), patch, test_action_buttons(), test_button_reboot(), test_button_share(), test_button_shutdown(), test_pinhandler_register_longpress() (+4 more)

### Community 58 - "Acquisition API Tests"
Cohesion: 0.26
Nodes (15): asyncio, capture(), patch, TestClient, test_aquire_multiple_nomodechange(), test_aquire_multiple_withmodechange(), test_aquire_still_capturemode(), test_aquire_still_exception() (+7 more)

### Community 59 - "Plugin Hookspecs & Stats"
Cohesion: 0.22
Nodes (11): SynchronizerConfig, Synchronizer, fixture, Create a SynchronizerRclone with mocked config + mocked rclone client., sync(), test_collection_hooks(), test_copy_sharepage_to_remotes(), test_get_share_links_public() (+3 more)

### Community 60 - "simple cluster"
Cohesion: 0.18
Nodes (9): api_delete_calibration_delete(), delete, Image, Reset calibration data., Compute the common overlapping crop region across all cameras. Returns (x1, y1,…, Specialized calibration manager., Crop a Pillow image to the given rectangle. Args: img (Image.Image): Input PIL…, align all images, while 1 image per camera, sorted by the index (+1 more)

### Community 61 - "AI Runtime Rules & Templates"
Cohesion: 0.14
Nodes (15): ADR Template, Execution Report Template, docs/ai/plan-template.md, Plan Template (short form), QA Report Template, Review Report Template, uv run poe agents:lint, Agent Contract Validation (+7 more)

### Community 62 - "filter_pilgram2 cluster"
Cohesion: 0.25
Nodes (7): available_filter, FilterPilgram2Config, FilterPilgram2, hookimpl, Image, filter_pilgram2_plugin(), fixture

### Community 63 - "baseconfig cluster"
Cohesion: 0.16
Nodes (6): BaseSettings, PydanticBaseSettingsSource, BaseConfig, Remove allof that would interfere with the normal processing of jsonforms…, Get schema to build UI. Schema is polished to the needs of UI, Persist config to file

### Community 64 - "Acquisition API"
Cohesion: 0.18
Nodes (12): api_cmd_aquisition_capturemode_get(), api_multicam_get(), api_multicam_loadfile_get(), api_still_get(), get, Path, set backends to preview or capture mode (usually automatically switched as…, video_stream() (+4 more)

### Community 65 - "repeatedtimer cluster"
Cohesion: 0.16
Nodes (6): Repeat Timer in separate thread for tasks to be executed in intervals, Call a function after a specified number of seconds: t = Timer(30.0, f,…, Stop the timer if it hasn't finished yet., RepeatedTimer, Timer, Thread

### Community 66 - "Container, Schemas & SSE"
Cohesion: 0.16
Nodes (6): BaseModel, basic class for sse events, SseEventBase, SseEventIntervalInformationRecord, SseEventLogRecord, SseEventOnetimeInformationRecord

### Community 67 - "base cluster"
Cohesion: 0.21
Nodes (7): CalibrationBase, Path, T, Base class providing save/load functionality for calibration data., Return the filename for a given camera index., Save all calibration data to disk., Load all calibration data from disk, to be invoked from inheriting class…

### Community 68 - "encode_animation_test cluster"
Cohesion: 0.21
Nodes (14): dummy_images(), library(), pillow_encode_avif(), pillow_encode_gif(), pillow_encode_webp(), Any, benchmark, fixture (+6 more)

### Community 69 - "sse_ cluster"
Cohesion: 0.18
Nodes (8): Request, get, Eventstream to feed clients with server generated events and data, subscribe(), class providing central sse, Client, Class each individual client connected, SseService

### Community 70 - "tdd_gate cluster"
Cohesion: 0.31
Nodes (13): changed_entries(), collect_names(), GateError, git(), main(), Exception, CI TDD gate for pull requests. Rules: docs/ai/testing-strategy.md "Strict TDD".…, Runs the PR's test files against the merge-base source in a throwaway worktree. (+5 more)

### Community 71 - "Share Config Group"
Cohesion: 0.24
Nodes (12): GroupShare, AppConfig class providing central config, Configure share or print actions., Configure additional parameter for the share command to input by the user., ShareProcessingParameters, GpioTrigger, KeyboardTrigger, BaseModel (+4 more)

### Community 72 - "charuco_board cluster"
Cohesion: 0.25
Nodes (12): generate_board(), get_detector(), CharucoDetector, ndarray, Size: (SquaresX, SquaresY), while X is left-right (width/columns) and Y top-…, Size: (SquaresX/Cols, SquaresY/Rows), while X is left-right and Y is top-bottom, dummy_charuco_images(), fixture (+4 more)

### Community 73 - "scale_image_test cluster"
Cohesion: 0.24
Nodes (13): cv2_scale(), image(), image_hires(), image_lores(), library(), pillow_scale(), benchmark, fixture (+5 more)

### Community 74 - "stream_lores_test cluster"
Cohesion: 0.26
Nodes (13): benchmark, pyav_cv2_scale(), pyav_pillow_scale(), pyav_scale_cv2_encode(), pyav_scale_simplejpeg_encode(), pyav_simplejpeg_scale(), pyav_turbojpeg_scale(), test_pyav_cv2_scale() (+5 more)

### Community 75 - "test_system cluster"
Cohesion: 0.24
Nodes (13): fixture, patch, TestClient, system_host_endpoint(), system_nonexistant_endpoint(), system_service_endpoint(), system_systemctl_endpoint(), system_systemctl_installuninstall_endpoint() (+5 more)

### Community 76 - "Plugin Hookspecs & Stats"
Cohesion: 0.22
Nodes (6): RcloneApi, Returns set of removable drives detected on the computer., Stats, ThreadedRegularSync, get_corresponding_remote_file(), Path

### Community 77 - "Admin Auth (JWT)"
Cohesion: 0.19
Nodes (12): api_get_config_current_active(), api_get_config_schema(), api_get_configurables(), api_post_config_current(), api_reset_all_config(), api_reset_config(), Any, AnyStr (+4 more)

### Community 78 - "BaseService"
Cohesion: 0.24
Nodes (4): BaseService, EnumStatus, Enum, All services (factory/singleton) and resources derive from this base class…

### Community 79 - "test_filter cluster"
Cohesion: 0.26
Nodes (11): Example 2nd-level subpackage., TestClient, test_apply_filter(), test_apply_filter_nonexistentfilter(), test_get_avail_filter(), test_get_avail_filter_err(), test_preview_filter_1977(), test_preview_filter_nonexistentfilter() (+3 more)

### Community 82 - "simple cluster"
Cohesion: 0.23
Nodes (8): CharucoDetector, ndarray, Path, Aggregate detections from multiple images of the same camera. Returns stacked…, Compute homography between reference and current camera using common ChArUco…, Calibrate one camera against the reference and save homography., Load all calibration data from disk., Calibrate all cameras against the reference camera. cameras[0] is all images…

### Community 83 - "Persona Prompts"
Cohesion: 0.18
Nodes (8): fastapi-backend-dev persona prompt, security-auditor persona prompt, web-frontend-dev persona prompt, API auth model (/api open, /api/admin JWT), context-refresh doc, api-contracts doc, Required PR structure, TDD-Waiver / Migration-Waiver PR lines

### Community 84 - "misc cluster"
Cohesion: 0.20
Nodes (9): field_serializer, GroupCommon, BaseModel, SerializationInfo, AppConfig class providing central config, Common config for photobooth., contextual_serializer_password(), Any (+1 more)

### Community 85 - "crop_image_test cluster"
Cohesion: 0.24
Nodes (8): image(), image_hires(), image_lores(), library(), benchmark, fixture, test_libraries_encode_hires(), test_libraries_encode_lores()

### Community 86 - "base cluster"
Cohesion: 0.27
Nodes (6): PathLike, CalibrationDataExtrinsics, CalibrationDataIntrinsics, PersistableDataclass, CalDataAlign, Set identity caldata so output will not be modified at all but useful in testing

### Community 87 - "Plugin Hookspecs & Stats"
Cohesion: 0.29
Nodes (9): Common, OndemandShareConfig, BaseModel, RcloneConfig, RemoteConfig, ShareConfig, RcloneApi, test_immediateSnycPipeline_skip_delete_op_when_upload_only_is_enabled() (+1 more)

### Community 88 - "abstractbackend cluster"
Cohesion: 0.22
Nodes (5): Framerate, public api, non-blocking, call by backends implementation when frame is delivered, so the fps can be…, Thread-safe rolling-window FPS calculator., Return remaining nanoseconds until the next frame should be processed. Positive…

### Community 90 - "printer cluster"
Cohesion: 0.33
Nodes (10): classify_linux(), classify_windows(), get_printer_status(), get_printer_status_linux(), get_printer_status_windows(), monitor_printer(), on_state_change(), PrinterStateChange (+2 more)

### Community 91 - "test_multicamera cluster"
Cohesion: 0.38
Nodes (10): patch, Path, TestClient, test_delete_calibration_success(), test_generate_charucoboard_failure(), test_generate_charucoboard_success(), test_get_result_failure(), test_get_result_success() (+2 more)

### Community 92 - "misc cluster"
Cohesion: 0.29
Nodes (9): le, Query, api_gallery_delete(), api_gallery_delete_all(), api_getitem(), api_getitems(), delete, get (+1 more)

### Community 93 - "image cluster"
Cohesion: 0.27
Nodes (6): RembgModelType, draw_rotated_text(), Image, Draw text at an angle into an image, takes the same arguments as Image.text()…, RemovebgStep, test_rembg_ai_stage()

### Community 94 - "__init__ cluster"
Cohesion: 0.36
Nodes (6): DisplayEnum, GenericStats, StrEnum, SubList, SubStats, class providing central plugin repo

### Community 95 - "Plugin Hookspecs & Stats"
Cohesion: 0.31
Nodes (3): hookimpl, Path, UUID

### Community 96 - "Processing API"
Cohesion: 0.24
Nodes (5): CountdownTimer, test that 0 countdown doesn't block whole application, check that timer is accurate enough, test_countdowntimer_accuracy(), test_countdowntimer_zero()

### Community 97 - "media cluster"
Cohesion: 0.42
Nodes (8): head, api_getitems_get(), api_getitems_head(), DimensionTypes, get, UUID, head used for download portal to check if the file is available without…, _serve_media_item()

### Community 98 - "resize_algorithm_test cluster"
Cohesion: 0.33
Nodes (8): parametrize, Resampling, cv2_resize(), pil_resize(), benchmark, Image, test_cv2_resize(), test_pil_resize()

### Community 99 - "BaseService"
Cohesion: 0.22
Nodes (3): skipif, SystemService, test_systemd_control()

### Community 100 - "Processing Event Hooks"
Cohesion: 0.44
Nodes (3): PluginEventHooks, Event, State

### Community 101 - "offset_image_test cluster"
Cohesion: 0.31
Nodes (8): image_hires_rgb(), benchmark, fixture, Image, recenter_image(), recenter_image_chops(), test_recenter_image(), test_recenter_image_chops()

### Community 102 - "scale_video_test cluster"
Cohesion: 0.33
Nodes (8): ffmpeg_h264_scale(), benchmark, fixture, pyav_h264_scale(), test_ffmpeg_h264_scale(), test_pyav_scale(), thread_type(), threading_number()

### Community 103 - "test_actions cluster"
Cohesion: 0.39
Nodes (8): TestClient, test_chose_1pic(), test_chose_1pic_occupied(), test_chose_1pic_otherexception(), test_chose_animation(), test_chose_collage(), test_chose_multicamera(), test_chose_video()

### Community 104 - "AI Engineering Workflows"
Cohesion: 0.32
Nodes (6): Autonomous Engineering Layer (.ai-engineering), autonomous-engineering.yaml config, doc link test (test_doc_links.py), Activation states PILOT_FROZEN/ACTIVE/RELEASE_FROZEN, Bootstrap validation workflow, Pilot mode (PILOT_FROZEN)

### Community 105 - "project-memory cluster"
Cohesion: 0.32
Nodes (8): Lessons Learned, Project Memory, PILOT_FROZEN activation state, config/autonomous-engineering.yaml, Scheduler Rules, docs/ai/autonomous-engineering.md, Work Orders (Tasks.md), Task Template

### Community 106 - "processing cluster"
Cohesion: 0.32
Nodes (3): JobModelType, FrontendNotifierEventHooks, SseEventProcessStateinfo

### Community 107 - "tdd_red_guard cluster"
Cohesion: 0.46
Nodes (7): git(), main(), marker_problem(), Path, Claude Code PreToolUse hook: blocks writes to src/photobooth logic until `uv…, The target may not exist yet (Write of a new file); resolve through the nearest…, resolve_target()

### Community 108 - "Abstract Camera Backend"
Cohesion: 0.25
Nodes (4): Path, A standalone video recorder that: - runs in its own thread - pulls lores frames…, Start recording. Returns the output filepath., SoftwareVideoRecorder

### Community 109 - "encode_video_test cluster"
Cohesion: 0.36
Nodes (7): process_ffmpeg(), process_pyav(), benchmark, fixture, run_around_tests(), test_process_ffmpeg(), test_process_pyav()

### Community 110 - "AI Engineering Workflows"
Cohesion: 0.33
Nodes (7): Daily Cycle workflow, Feature Development workflow, Release Process workflow, Review Process workflow, Agent roles (PM, Architect, Coordinator, Implementer, Reviewer, QA, Reporter), Human approval gate (WAITING_APPROVAL, PILOT_FROZEN), Task state machine (NEW to REPORTED)

### Community 111 - "multicamera cluster"
Cohesion: 0.33
Nodes (7): api_get_calibration_generate_charucoboard(), api_post_calibrate_all(), CalibrationRequest, CharucoBoardDefinition, BaseModel, post, Post files to calculate a new calibration, save it and reload services to apply…

### Community 112 - "test_share cluster"
Cohesion: 0.48
Nodes (6): TestClient, test_get_limits_reset(), test_get_limits_reset_error(), test_get_limits_reset_nonexistant_failsilent(), test_get_stats_reset_all(), test_get_stats_reset_all_error()

### Community 115 - "test_information cluster"
Cohesion: 0.53
Nodes (5): TestClient, test_get_limits_reset(), test_get_limits_reset_error(), test_get_stats_reset(), test_get_stats_reset_all_error()

### Community 116 - "test_static cluster"
Cohesion: 0.53
Nodes (5): TestClient, test_private_css(), test_private_css_nonexisting_placeholder(), test_read_web_sharepage(), test_read_web_spa()

### Community 117 - "test_tdd_lib cluster"
Cohesion: 0.50
Nodes (5): classify_changes(), entries: [{"status": "A"|"M"|"D"|"R087"..., "path": ...}] as from `git diff…, entry(), test_edge_classify_groups_each_kind(), test_edge_classify_ignores_deletes_and_pure_renames()

### Community 118 - "App Factory & Startup"
Cohesion: 0.40
Nodes (5): index(), get, if private.css exists return the file content, otherwise send empty response to…, Serve index.html with forced revalidation (ETag checked every time)., ui_private_css()

### Community 119 - "misc cluster"
Cohesion: 0.40
Nodes (4): GroupMediaprocessing, BaseModel, AppConfig class providing central config, Configure stages how to process images after capture.

### Community 120 - "misc cluster"
Cohesion: 0.40
Nodes (4): GroupMisc, BaseModel, AppConfig class providing central config, Quite advanced or experimental, usually not necessary to touch. Can change any…

### Community 123 - "filter_pilgram2_test cluster"
Cohesion: 0.40
Nodes (4): filter_algo(), benchmark, fixture, test_pilgram_lores_benchmark()

### Community 124 - "test_enumerate cluster"
Cohesion: 0.60
Nodes (4): TestClient, test_admin_enumerate_files(), test_admin_enumerate_serialports(), test_admin_enumerate_usbcameras()

### Community 125 - "tdd_lib cluster"
Cohesion: 0.50
Nodes (4): parse_junit_failures(), Reads pytest --junitxml. A collection failure (usually a module that does not…, test_edge_junit_collection_failure_is_file_level(), test_error_parse_junit_failures_on_empty_or_invalid_xml()

### Community 127 - "GPIO Lights Plugin"
Cohesion: 0.50
Nodes (3): contextual_serializer_password(), Any, SerializationInfo

### Community 128 - "test_debug cluster"
Cohesion: 0.67
Nodes (3): TestClient, test_read_log(), test_read_log_err()

### Community 129 - "project-memory cluster"
Cohesion: 0.67
Nodes (3): Validation Auto-Fix Prompt, BLOCKED_HUMAN state, Bootstrap Repair Loop

## Knowledge Gaps
- **76 isolated node(s):** `new-task-worktree.sh script`, `architect`, `product-manager`, `operating-model`, `Lessons Learned` (+71 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **27 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `JobModelBase` connect `Processing Event Hooks` to `App Config & Acquisition Wiring`, `Processing Event Hooks`, `Actions Config Group`, `Media Collection Service`, `DB Models & Alembic`, `multicamera cluster`, `video cluster`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Why does `BaseService` connect `BaseService` to `DB Models & Alembic`, `App Config & Acquisition Wiring`, `Information Service`, `share cluster`, `Processing Event Hooks`, `Media Collection Service`, `Service Container Lifecycle`, `BaseService`, `processing cluster`, `Plugin Manager`, `Configuration Service`, `Logging Service`, `Processing Service`, `Acquisition Service`, `gpio cluster`, `gpio cluster`, `GPIO Pin Handling`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **Why does `AcquisitionService` connect `Acquisition Service` to `DB Models & Alembic`, `App Config & Acquisition Wiring`, `Information Service`, `repeatedtimer cluster`, `Processing Event Hooks`, `Media Collection Service`, `Actions Config Group`, `processing cluster`, `BaseService`, `DB Models & Alembic`, `multicamera cluster`, `video cluster`, `Processing Service`, `Acquisition API Tests`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `AcquisitionService` (e.g. with `BaseService` and `InformationService`) actually correct?**
  _`AcquisitionService` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `AbstractBackend` (e.g. with `StoppableThread` and `DigicamcontrolBackend`) actually correct?**
  _`AbstractBackend` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `JobModelBase` (e.g. with `JobModelAnimation` and `CaptureSet`) actually correct?**
  _`JobModelBase` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `MediacollectionService` (e.g. with `BaseService` and `Button`) actually correct?**
  _`MediacollectionService` has 8 INFERRED edges - model-reasoned connections that need verification._