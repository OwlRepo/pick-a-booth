# Graph Report - .  (2026-10-13)

## Corpus Check
- 356 files · ~101,720 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2692 nodes · 5773 edges · 159 communities (140 shown, 19 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 330 edges (avg confidence: 0.61)
- Token cost: 304,559 input · 0 output

## Community Hubs (Navigation)
- Plugin Hookspecs & Stats
- TDD Test Repo Fixture
- Admin Files & Enumerate API
- Background Removal (rembg)
- Media Collection Service
- App Config & Acquisition Wiring
- DB Models & Alembic
- Container, Schemas & SSE
- Commander Plugin
- Admin Auth (JWT)
- Image Processing Steps
- Abstract Camera Backend
- Service Container Lifecycle
- Image/Animation Benchmarks
- Processing Event Hooks
- Processing API
- Media Pipeline Core
- App Factory & Startup
- Collage/Animation Merge
- Share Config Group
- AI Workflow Phase Docs
- Filter API
- Acquisition Service
- AI Engineering Agents
- GPIO Lights Plugin
- Picamera2 Tests
- Acquisition API
- Wigglecam Backend
- Multicamera Steps
- Gphoto2 Backend
- Webcam/Virtual Backends
- Encode Benchmarks
- Backend Mode Controller
- BaseService
- Information Service
- AI Engineering Workflows
- WLED Plugin
- Picamera2 Backend
- Virtual Camera Source
- Actions Config Group
- TDD Name Rules
- Config Admin Tests
- Persona Prompts
- PyAV Webcam Backend
- GPIO Pin Handling
- TDD Lib & Bash Guard
- digiCamControl Backend
- AI Runtime Rules & Templates
- Acquisition Hookspec
- Rclone Synchronizer
- Processing Service
- Share-on-Demand PHP
- Plugin Manager
- WLED Config
- Configuration Service
- TDD Red CLI
- Acquisition API Tests
- Logging Service
- Persona Generator
- V4L Webcam Backend
- base cluster
- resilientservice cluster
- project-memory cluster
- filter_pilgram2 cluster
- baseconfig cluster
- sse_ cluster
- misc cluster
- simple cluster
- encode_animation_test cluster
- tdd_gate cluster
- __init__ cluster
- abstractbackend cluster
- repeatedtimer cluster
- image cluster
- charuco_board cluster
- scale_image_test cluster
- stream_lores_test cluster
- test_system cluster
- gpio cluster
- test_filter cluster
- multicamera cluster
- video cluster
- simple cluster
- resilientservice cluster
- misc cluster
- multicamera cluster
- animation cluster
- crop_image_test cluster
- base cluster
- __init__ cluster
- gpio cluster
- share cluster
- printer cluster
- test_multicamera cluster
- misc cluster
- media cluster
- resize_algorithm_test cluster
- image cluster
- __init__ cluster
- __init__ cluster
- offset_image_test cluster
- scale_video_test cluster
- test_actions cluster
- processing cluster
- tdd_red_guard cluster
- encode_video_test cluster
- conftest cluster
- media_encode cluster
- test_share cluster
- test_information cluster
- test_static cluster
- test_tdd_lib cluster
- filter_pilgram2_test cluster
- test_enumerate cluster
- tdd_lib cluster
- base_plugin cluster
- test_debug cluster
- CONTRIBUTING cluster
- actions cluster
- actions cluster
- actions cluster
- actions cluster
- eod-report cluster
- new-task-worktree cluster
- __init__ cluster
- __init__ cluster
- __init__ cluster
- bug_report cluster
- feature_request cluster
- pyproject cluster

## God Nodes (most connected - your core abstractions)
1. `Mediaitem` - 57 edges
2. `AcquisitionService` - 55 edges
3. `AbstractBackend` - 48 edges
4. `JobModelBase` - 47 edges
5. `MediacollectionService` - 44 edges
6. `make_repo()` - 43 edges
7. `BaseService` - 40 edges
8. `InformationService` - 36 edges
9. `run_script()` - 35 edges
10. `BaseSession` - 33 edges

## Surprising Connections (you probably didn't know these)
- `.ai-engineering repository-local AI workflow layer` --references--> `Feature Development workflow`  [INFERRED]
  AGENTS.md → .ai-engineering/workflows/feature-development.md
- `test_edge_find_bash_write_targets_detects_writes()` --calls--> `find_bash_write_targets()`  [INFERRED]
  scripts/tests/test_tdd_lib.py → scripts/ci/tdd_lib.py
- `Blocker Handling workflow` --references--> `AGENTS.md (core principles, canonical task flow, persona)`  [EXTRACTED]
  .ai-engineering/workflows/blocker-handling.md → AGENTS.md
- `Bug Fix workflow` --references--> `Strict TDD (tdd:red, tdd:gate)`  [EXTRACTED]
  .ai-engineering/workflows/bug-fix.md → AGENTS.md
- `Review Process workflow` --references--> `Strict TDD (tdd:red, tdd:gate)`  [EXTRACTED]
  .ai-engineering/workflows/review-process.md → AGENTS.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Agent role contracts** — ai_engineering_agents_product_manager, ai_engineering_agents_architect, ai_engineering_agents_coordinator, ai_engineering_agents_implementer, ai_engineering_agents_reviewer, ai_engineering_agents_qa, ai_engineering_agents_reporter [EXTRACTED 1.00]
- **Task lifecycle state docs** — ai_engineering_core_task_lifecycle, ai_engineering_core_task_state_machine, ai_engineering_core_task_state_machine_skipped_already_implemented, ai_engineering_core_task_state_machine_blocked_states, ai_engineering_core_task_state_machine_waiting_approval [INFERRED 0.85]
- **Agent role contracts** — ai_engineering_validation_agent_contract_tests_role_product_manager, ai_engineering_validation_agent_contract_tests_role_architect, ai_engineering_validation_agent_contract_tests_role_coordinator, ai_engineering_validation_agent_contract_tests_role_implementer, ai_engineering_validation_agent_contract_tests_role_reviewer, ai_engineering_validation_agent_contract_tests_role_qa, ai_engineering_validation_agent_contract_tests_role_reporter [EXTRACTED 1.00]
- **Validation and repair suite** — ai_engineering_validation_bootstrap_check_doc, ai_engineering_validation_repair_loop_doc, ai_engineering_validation_auto_fix_prompt_doc, ai_engineering_validation_workflow_tests_doc [INFERRED 0.85]
- **Report templates** — ai_engineering_templates_execution_report_doc, ai_engineering_templates_review_report_doc, ai_engineering_templates_qa_report_doc, ai_engineering_templates_pr_report_doc, ai_engineering_templates_eod_report_doc [INFERRED 0.75]
- **Phase-loaded AI workflow workflow docs** — _ai_engineering_workflows_task_intake, _ai_engineering_workflows_feature_development, _ai_engineering_workflows_review_process, _ai_engineering_workflows_release_process, _ai_engineering_workflows_bug_fix, _ai_engineering_workflows_blocker_handling, _ai_engineering_workflows_daily_cycle [INFERRED 0.85]
- **GitHub Actions CI workflows** — _github_workflows_ai_gates, _github_workflows_benchmarks, _github_workflows_cicd, _github_workflows_linter, _github_workflows_pytests [INFERRED 0.85]
- **Generated agent personas** — agents_src_prompts_accessibility_auditor, agents_src_prompts_code_reviewer, agents_src_prompts_db_architect, agents_src_prompts_fastapi_backend_dev, agents_src_prompts_project_manager, agents_src_prompts_security_auditor, agents_src_prompts_test_engineer, agents_src_prompts_ui_ux_designer, agents_src_prompts_web_frontend_dev [EXTRACTED 1.00]
- **Canonical task flow phase docs** — docs_ai_planning, docs_ai_execution, docs_ai_handoff, docs_ai_task_router [EXTRACTED 0.95]
- **Plan prompt templates** — docs_ai_prompts_bugfix_rca, docs_ai_prompts_bugfix_plan, docs_ai_prompts_feature_plan, docs_ai_prompts_refactor_plan [EXTRACTED 0.90]

## Communities (159 total, 19 thin omitted)

### Community 0 - "Plugin Hookspecs & Stats"
Cohesion: 0.05
Nodes (48): Protocol, DisplayEnum, GenericStats, StrEnum, SubList, SubStats, class providing central plugin repo, Common (+40 more)

### Community 1 - "TDD Test Repo Fixture"
Cohesion: 0.07
Nodes (64): git(), make_repo(), Path, Repo, run_script(), write(), cited_paths(), Path (+56 more)

### Community 2 - "Admin Files & Enumerate API"
Cohesion: 0.05
Nodes (59): Body, api_get_rclone_remotes(), api_get_serial_ports(), api_get_usbcameras(), get_search(), get, api_clearrecycledir(), create_upload_file() (+51 more)

### Community 3 - "Background Removal (rembg)"
Cohesion: 0.06
Nodes (36): SessionOptions, naive_cutout(), Any, PILImage, The util is very much inspired by https://github.com/danielgatis/rembg Thank…, Remove the background from an input image., remove(), new_session() (+28 more)

### Community 4 - "Media Collection Service"
Cohesion: 0.05
Nodes (47): MediacollectionService, UUID, Handle all image related stuff, DbListenter, client(), client_authenticated(), global_function_setup1(), global_function_setup2() (+39 more)

### Community 5 - "App Config & Acquisition Wiring"
Cohesion: 0.08
Nodes (20): AppConfig class providing central config, manage up to two photobooth-app backends in this module, MultiImageJobControl, Configure job control affecting the procedure., FrameOverlay, BaseModel, UUID, JobModelAnimation (+12 more)

### Community 6 - "DB Models & Alembic"
Cohesion: 0.06
Nodes (25): DeclarativeBase, listens_for, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Base, Cacheditem (+17 more)

### Community 7 - "Container, Schemas & SSE"
Cohesion: 0.06
Nodes (30): datetime, MediaitemPublic, BaseModel, ShareLimitsPublic, UsageStatsPublic, submit events on gpio pin interrups Pin Numbering:…, BaseModel, basic class for sse events (+22 more)

### Community 8 - "Commander Plugin"
Cohesion: 0.11
Nodes (31): eventHooks, field_validator, Commander, Event, hookimpl, MediaitemTypes, State, ThreadCommand (+23 more)

### Community 9 - "Admin Auth (JWT)"
Cohesion: 0.07
Nodes (44): oauth2_scheme, OAuth2PasswordRequestForm, login_for_access_token(), Depends, get, post, read_users_me(), api_get_config_current_active() (+36 more)

### Community 10 - "Image Processing Steps"
Cohesion: 0.12
Nodes (38): Color, TextsConfig, ImageContext, FillBackgroundStep, ImageFrameStep, ImageMountStep, NextStep, Path (+30 more)

### Community 11 - "Abstract Camera Backend"
Cohesion: 0.06
Nodes (22): AbstractBackend, BackendStats, MulticamRequest, ABC, Path, # TODO: validate 0.5 tolerance., defines some common stats - if backend supports, they return these properties,…, To start the backend to serve (+14 more)

### Community 12 - "Service Container Lifecycle"
Cohesion: 0.08
Nodes (29): Events, Container, stop all services first (reverse order), then start them again., GpioLights, Event, hookimpl, State, test_hooks_integration_start_stop_if_hook_implemented() (+21 more)

### Community 13 - "Image/Animation Benchmarks"
Cohesion: 0.07
Nodes (34): BytesIO, benchmark, test_transpose_piexif(), test_transpose_pillow(), transpose_piexif(), transpose_pillow(), ffmpeg_hq_optimizedquality_scale(), ffmpeg_hq_optimizedspeed_scale() (+26 more)

### Community 14 - "Processing Event Hooks"
Cohesion: 0.06
Nodes (16): PluginEventHooks, Event, State, JobModelBase, ABC, Event, UUID, eval user / automated input got from transition (+8 more)

### Community 15 - "Processing API"
Cohesion: 0.07
Nodes (27): BackgroundTasks, deprecated, api_cmd_abort_get(), api_cmd_confirm_get(), api_cmd_reject_get(), api_get_preview_image_filtered(), get, UUID (+19 more)

### Community 16 - "Media Pipeline Core"
Cohesion: 0.11
Nodes (22): Context, ErrorHandler, VideoContext, _default_error_handler(), Pipeline, PipelineCursor, PipelineError, PipelineStep (+14 more)

### Community 17 - "App Factory & Startup"
Cohesion: 0.08
Nodes (23): FastAPI, _create_app(), lifespan(), _create_basic_folders(), api_get_statscounter_reset_all(), api_get_statscounter_reset_field(), get, api_get_config_current_active() (+15 more)

### Community 18 - "Collage/Animation Merge"
Cohesion: 0.14
Nodes (20): PluginFilters, AnimationMergeDefinition, CollageMergeDefinition, BaseModel, CollageContext, process_and_generate_collage(), AddPredefinedImagesStep, PostPredefinedImagesStep (+12 more)

### Community 19 - "Share Config Group"
Cohesion: 0.10
Nodes (32): GroupShare, BaseModel, AppConfig class providing central config, Configure share or print actions., Configure additional parameter for the share command to input by the user., Configure options to share or print images., Configure stages how to process mediaitem before printing on paper., ShareConfigurationSet (+24 more)

### Community 20 - "AI Workflow Phase Docs"
Cohesion: 0.11
Nodes (15): SQLite and Alembic data model, No shared DEV server, Maps are not proof; code wins, Worktree and branch isolation, Completion Gate, Integration sequence, Phase-stop rule, Graphify discovery first (+7 more)

### Community 21 - "Filter API"
Cohesion: 0.11
Nodes (26): api_get_result(), api_applyfilter(), api_get_preview_image_filtered(), api_get_userselectable_filters(), get, patch, UUID, CollageProcessing (+18 more)

### Community 22 - "Acquisition Service"
Cohesion: 0.08
Nodes (19): AcquisitionService, Path, called by job processor when a countdown for video is started, called by job processor when a countdown for multicam is started, Gather stats from active backends. Backend stats are converted to dict to be…, called by job processor when a countdown for stills is started, _acqs(), fixture (+11 more)

### Community 23 - "AI Engineering Agents"
Cohesion: 0.11
Nodes (31): Autonomous Engineering Layer Setup, architect, coordinator, implementer, product-manager, qa, reporter, reviewer (+23 more)

### Community 24 - "GPIO Lights Plugin"
Cohesion: 0.08
Nodes (16): DigitalOutputDevice, GpioLight, GpioLightsConfig, BaseModel, AppDigitalOutputDevice, api_get_limitscounter_reset_all(), api_get_limitscounter_reset_field(), get (+8 more)

### Community 25 - "Picamera2 Tests"
Cohesion: 0.12
Nodes (26): webcameras(), backend_picamera2(), fixture, get lores and hires images from backend and assert, run_around_tests(), test_get_video_picamera2(), test_getImages(), backend_virtual() (+18 more)

### Community 26 - "Acquisition API"
Cohesion: 0.11
Nodes (25): api_cmd_aquisition_capturemode_get(), api_multicam_get(), api_multicam_loadfile_get(), api_still_get(), get, Path, set backends to preview or capture mode (usually automatically switched as…, video_stream() (+17 more)

### Community 27 - "Wigglecam Backend"
Cohesion: 0.12
Nodes (12): Path, Trigger a capture request and collect hi-res images from all cameras., Background loop to receive lores frames., # TODO: get highres from the one camera selected, for now get all and return…, WigglecamBackend, GroupCameraWigglecam, WigglecamNodes, backend_wigglecam() (+4 more)

### Community 28 - "Multicamera Steps"
Cohesion: 0.12
Nodes (17): MatLike, MulticameraContext, AutoPivotPointStep, CropCommonAreaStep, OffsetPerOpticalFlowStep, Image, NextStep, Align next_img to prev_img using optical flow of pivot point. (+9 more)

### Community 29 - "Gphoto2 Backend"
Cohesion: 0.12
Nodes (11): StillRequest, GpEvents, Gphoto2Backend, GpWidgets, Enum, Gphoto2Parameters, Configure different settings when switching between modes., backend_gphoto2() (+3 more)

### Community 30 - "Webcam/Virtual Backends"
Cohesion: 0.12
Nodes (18): model_validator, BaseModelCamera, GroupBackend, GroupCameraGphoto2, GroupCameraPicamera2, GroupCameraPyav, GroupCameras, GroupCameraV4l2 (+10 more)

### Community 31 - "Encode Benchmarks"
Cohesion: 0.13
Nodes (22): cv2_encode_jpg(), cv2_encode_png_lossless(), cv2_encode_webp(), image(), image_hires(), image_lores(), library(), library_yuv420() (+14 more)

### Community 32 - "Backend Mode Controller"
Cohesion: 0.10
Nodes (11): Modes, ModeController, Einfacher Mode-Controller mit: - requested_mode (Thread-agnostisch) -…, usually requested when creating a video but also for livestream. livestream…, Monitor thread function to request standby if no livestream is requested for…, Wird im stream-thread aufgerufen, wenn es passend für einen potentiellen mode-…, called during device setup, called internally by supervising if liveview frames are requested (+3 more)

### Community 33 - "BaseService"
Cohesion: 0.12
Nodes (8): skipif, BaseService, EnumStatus, Enum, Base service and resources module., All services (factory/singleton) and resources derive from this base class…, SystemService, test_systemd_control()

### Community 34 - "Information Service"
Cohesion: 0.13
Nodes (3): InformationService, Any, Raspberry Pi system health monitor using vcgencmd. Decode throttled bitmask…

### Community 35 - "AI Engineering Workflows"
Cohesion: 0.09
Nodes (25): Blocker Handling workflow, Bug Fix workflow, Daily Cycle workflow, Feature Development workflow, Release Process workflow, Review Process workflow, Task Intake workflow, Dependabot config (pip + github-actions, target dev) (+17 more)

### Community 36 - "WLED Plugin"
Cohesion: 0.15
Nodes (6): Event, hookimpl, State, To start the resilient service, To stop the resilient service, Wled

### Community 37 - "Picamera2 Backend"
Cohesion: 0.11
Nodes (6): Picamera2Backend, Path, Every camera tuning file usually has at least "normal", "short" and "long"…, function that returns None if value is None, otherwise round is applied and…, picamera2 has local start_recording, which overrides the abstract class…, on start set autofocus to continuous if requested by config or auto and trigger…

### Community 38 - "Virtual Camera Source"
Cohesion: 0.13
Nodes (6): FolderImageSource, Path, for other threads to receive a hq JPEG image, Read all JPEGs from a folder, mmap them once, and cycle endlessly., VirtualCameraBackend, test_optimize_mode()

### Community 39 - "Actions Config Group"
Cohesion: 0.16
Nodes (22): AnimationProcessing, BaseConfigurationSet, GroupActions, MulticameraJobControl, BaseModel, Configure job control affecting the procedure., Configure stages how to process collage after capture., Configure stages how to process collage after capture. (+14 more)

### Community 40 - "TDD Name Rules"
Cohesion: 0.15
Nodes (22): check_names(), extract_test_names(), judge_red(), parse_waivers(), added: names introduced by the diff (any file). new_files: full ordered names…, Test functions pytest would collect, in declaration order. Strings, comments…, added(), test_edge_extract_handles_async_methods_and_skips_fixtures() (+14 more)

### Community 41 - "Config Admin Tests"
Cohesion: 0.14
Nodes (19): AppConfig, AppConfig class glueing all together In the case where a value is specified for…, patch, TestClient, test_config_endpoints_ui(), test_config_getschema(), test_config_patch(), test_config_post_validationerror() (+11 more)

### Community 42 - "Persona Prompts"
Cohesion: 0.12
Nodes (21): accessibility-auditor persona prompt, code-reviewer persona prompt, db-architect persona prompt, fastapi-backend-dev persona prompt, project-manager persona prompt, security-auditor persona prompt, test-engineer persona prompt, ui-ux-designer persona prompt (+13 more)

### Community 43 - "PyAV Webcam Backend"
Cohesion: 0.12
Nodes (7): InputContainer, Packet, WebcamPyavBackend, PermanentFault, Raised from within the services when the service should not attempt recovery., test_optimize_mode(), VideoStream

### Community 44 - "GPIO Pin Handling"
Cohesion: 0.17
Nodes (15): PinHandler, gpio_service(), pinhandler1(), fixture, patch, test_action_buttons(), test_button_reboot(), test_button_share() (+7 more)

### Community 45 - "TDD Lib & Bash Guard"
Cohesion: 0.13
Nodes (20): expr, find_bash_write_targets(), _is_fixture(), is_guarded_source(), _is_path_arg(), kind_of(), NamedTuple, Shared rules for the TDD gate (CI), `uv run poe tdd:red` (local) and the Claude… (+12 more)

### Community 46 - "digiCamControl Backend"
Cohesion: 0.13
Nodes (8): HTTPServer, DigicamcontrolBackend, r""" Digicamcontrol backend implementation Quirks: - using webfrontend only…, GroupCameraDigicamcontrol, backend_digicamcontrol_emulated(), fixture, test_emulated_get_images_disable_liveview_recovery_more_retries(), test_optimize_mode()

### Community 47 - "AI Runtime Rules & Templates"
Cohesion: 0.12
Nodes (20): Claude Code Runtime Rules, tdd_red_guard.py PreToolUse hook, Codex Runtime Rules, uv run poe tdd:red, CI tdd:gate backstop, ADR Template, Execution Report Template, docs/ai/plan-template.md (+12 more)

### Community 48 - "Acquisition Hookspec"
Cohesion: 0.14
Nodes (11): hookspec, PluginAcquisitionSpec, triggers at the start of a still countdown event, triggers before a shot, triggers before a still only, triggers before a video only, triggers before a multicam still only, triggers after a capture still event (+3 more)

### Community 49 - "Rclone Synchronizer"
Cohesion: 0.11
Nodes (10): RcloneApi, UUID, setup the resource right before run_service logic, tear down the resource right after run_service logic and in case of crashes, service logic to be run when the service is started, ShareOnDemandService, start service and try to download an image that does not exist, test some common actions on url (+2 more)

### Community 50 - "Processing Service"
Cohesion: 0.15
Nodes (5): ProcessingService, ActionType, if queue is initialized on _external_cmd_queue, a user request is waited for., Thread, userEvents

### Community 51 - "Share-on-Demand PHP"
Cohesion: 0.22
Nodes (3): RuntimeException, AuthException, ShareService

### Community 52 - "Plugin Manager"
Cohesion: 0.15
Nodes (7): BasePlugin, PluginManagerService, When the pluginmanager is started, it will start all registered plugins that…, When the pluginmanager is stoppped, it will stop all registered plugins that…, pluginmanager_service(), fixture, test_list_plugins()

### Community 53 - "WLED Config"
Cohesion: 0.14
Nodes (15): Common, BaseModel, WledConfig, Enum, WledPreset, fixture, should just fail in silence if disabled but app triggers some presets, should just fail in silence if disabled but app triggers some presets (+7 more)

### Community 54 - "Configuration Service"
Cohesion: 0.18
Nodes (7): ConfigurationService, Any, AnyStr, configuration_service(), fixture, test_plugin_config_get_current(), test_plugin_config_get_schema()

### Community 55 - "TDD Red CLI"
Cohesion: 0.22
Nodes (15): changed_entries(), git(), main(), parse_args(), Exception, Path, `uv run poe tdd:red`: run this branch's changed tests BEFORE implementing and…, Committed + staged + unstaged changes against the merge-base, plus untracked… (+7 more)

### Community 56 - "Acquisition API Tests"
Cohesion: 0.26
Nodes (15): asyncio, capture(), patch, TestClient, test_aquire_multiple_nomodechange(), test_aquire_multiple_withmodechange(), test_aquire_still_capturemode(), test_aquire_still_exception() (+7 more)

### Community 57 - "Logging Service"
Cohesion: 0.15
Nodes (6): ExceptHookArgs, LogRecord, EventstreamLogHandler, LoggingService, mute some logger by rasing their log level, Logging handler to emit events to eventstream; to be displayed in console.log…

### Community 58 - "Persona Generator"
Cohesion: 0.33
Nodes (15): Persona, check(), claude_file(), codex_file(), compute_targets(), _escape(), find_duplicate_owned_globs(), generate() (+7 more)

### Community 59 - "V4L Webcam Backend"
Cohesion: 0.16
Nodes (3): Convert JPG/MJPG and YUVY pixelformat to output JPG, WebcamV4lBackend, test_optimize_mode()

### Community 60 - "base cluster"
Cohesion: 0.19
Nodes (8): CalibrationDataExtrinsics, CalibrationDataIntrinsics, CalibrationBase, PersistableDataclass, Base class providing save/load functionality for calibration data., Save all calibration data to disk., CalDataAlign, Set identity caldata so output will not be modified at all but useful in testing

### Community 61 - "resilientservice cluster"
Cohesion: 0.20
Nodes (9): CrashReporter, ABC, Exception, QuietCrashReporter, Raised when the service probably only crashes temporarily and there is a chance…, Raised when the service probably crashes permanently and will do so after a…, ServiceCrashedPermanently, ServiceCrashedTemporarily (+1 more)

### Community 62 - "project-memory cluster"
Cohesion: 0.17
Nodes (15): Lessons Learned, Project Memory, PILOT_FROZEN activation state, config/autonomous-engineering.yaml, Scheduler Rules, docs/ai/autonomous-engineering.md, Work Orders (Tasks.md), Task Template (+7 more)

### Community 63 - "filter_pilgram2 cluster"
Cohesion: 0.25
Nodes (7): available_filter, FilterPilgram2Config, FilterPilgram2, hookimpl, Image, filter_pilgram2_plugin(), fixture

### Community 64 - "baseconfig cluster"
Cohesion: 0.16
Nodes (6): BaseSettings, PydanticBaseSettingsSource, BaseConfig, Remove allof that would interfere with the normal processing of jsonforms…, Get schema to build UI. Schema is polished to the needs of UI, Persist config to file

### Community 65 - "sse_ cluster"
Cohesion: 0.16
Nodes (8): Request, get, Eventstream to feed clients with server generated events and data, subscribe(), class providing central sse, Client, Class each individual client connected, SseService

### Community 66 - "misc cluster"
Cohesion: 0.15
Nodes (12): AppConfig class providing central config file called appconfig_ to avoid…, GroupMediaprocessing, BaseModel, AppConfig class providing central config, Configure stages how to process images after capture., GroupMisc, BaseModel, AppConfig class providing central config (+4 more)

### Community 67 - "simple cluster"
Cohesion: 0.20
Nodes (7): Image, Reset calibration data., Compute the common overlapping crop region across all cameras. Returns (x1, y1,…, Specialized calibration manager., Crop a Pillow image to the given rectangle. Args: img (Image.Image): Input PIL…, align all images, while 1 image per camera, sorted by the index, SimpleCalibrationUtil

### Community 68 - "encode_animation_test cluster"
Cohesion: 0.21
Nodes (14): dummy_images(), library(), pillow_encode_avif(), pillow_encode_gif(), pillow_encode_webp(), Any, benchmark, fixture (+6 more)

### Community 69 - "tdd_gate cluster"
Cohesion: 0.31
Nodes (13): changed_entries(), collect_names(), GateError, git(), main(), Exception, CI TDD gate for pull requests. Rules: docs/ai/testing-strategy.md "Strict TDD".…, Runs the PR's test files against the merge-base source in a throwaway worktree. (+5 more)

### Community 70 - "__init__ cluster"
Cohesion: 0.27
Nodes (9): PluginStatemachineSpec, Event, MediaitemTypes, State, job processor before a transition takes place. for details see python…, job processor when exit a state. for details see python statemachine library, job processor on the transition. for details see python statemachine library, job processor when the new state is entered. for details see python… (+1 more)

### Community 71 - "abstractbackend cluster"
Cohesion: 0.16
Nodes (7): Framerate, LoresBroadcastRes, Orientation, public api, non-blocking, call by backends implementation when frame is delivered, so the fps can be…, Thread-safe rolling-window FPS calculator., Return remaining nanoseconds until the next frame should be processed. Positive…

### Community 72 - "repeatedtimer cluster"
Cohesion: 0.18
Nodes (5): Repeat Timer in separate thread for tasks to be executed in intervals, Call a function after a specified number of seconds: t = Timer(30.0, f,…, Stop the timer if it hasn't finished yet., RepeatedTimer, Timer

### Community 74 - "charuco_board cluster"
Cohesion: 0.25
Nodes (12): generate_board(), get_detector(), CharucoDetector, ndarray, Size: (SquaresX, SquaresY), while X is left-right (width/columns) and Y top-…, Size: (SquaresX/Cols, SquaresY/Rows), while X is left-right and Y is top-bottom, dummy_charuco_images(), fixture (+4 more)

### Community 75 - "scale_image_test cluster"
Cohesion: 0.24
Nodes (13): cv2_scale(), image(), image_hires(), image_lores(), library(), pillow_scale(), benchmark, fixture (+5 more)

### Community 76 - "stream_lores_test cluster"
Cohesion: 0.26
Nodes (13): benchmark, pyav_cv2_scale(), pyav_pillow_scale(), pyav_scale_cv2_encode(), pyav_scale_simplejpeg_encode(), pyav_simplejpeg_scale(), pyav_turbojpeg_scale(), test_pyav_cv2_scale() (+5 more)

### Community 77 - "test_system cluster"
Cohesion: 0.24
Nodes (13): fixture, patch, TestClient, system_host_endpoint(), system_nonexistant_endpoint(), system_service_endpoint(), system_systemctl_endpoint(), system_systemctl_installuninstall_endpoint() (+5 more)

### Community 79 - "test_filter cluster"
Cohesion: 0.26
Nodes (11): Example 2nd-level subpackage., TestClient, test_apply_filter(), test_apply_filter_nonexistentfilter(), test_get_avail_filter(), test_get_avail_filter_err(), test_preview_filter_1977(), test_preview_filter_nonexistentfilter() (+3 more)

### Community 82 - "simple cluster"
Cohesion: 0.23
Nodes (8): CharucoDetector, ndarray, Path, Aggregate detections from multiple images of the same camera. Returns stacked…, Compute homography between reference and current camera using common ChArUco…, Calibrate one camera against the reference and save homography., Load all calibration data from disk., Calibrate all cameras against the reference camera. cameras[0] is all images…

### Community 83 - "resilientservice cluster"
Cohesion: 0.21
Nodes (4): setup the resource right before run_service logic, tear down the resource right after run_service logic and in case of crashes, service logic to be run when the service is started, ResilientService

### Community 84 - "misc cluster"
Cohesion: 0.20
Nodes (9): field_serializer, GroupCommon, BaseModel, SerializationInfo, AppConfig class providing central config, Common config for photobooth., contextual_serializer_password(), Any (+1 more)

### Community 85 - "multicamera cluster"
Cohesion: 0.23
Nodes (11): api_delete_calibration_delete(), api_get_calibration_generate_charucoboard(), api_get_calibration_stats(), api_post_calibrate_all(), CalibrationRequest, CharucoBoardDefinition, BaseModel, delete (+3 more)

### Community 86 - "animation cluster"
Cohesion: 0.29
Nodes (6): AnimationContext, process_and_generate_animation(), AlignSizesStep, NextStep, Testing Mediaprocessing collage, test_align_sizes_stage()

### Community 87 - "crop_image_test cluster"
Cohesion: 0.24
Nodes (8): image(), image_hires(), image_lores(), library(), benchmark, fixture, test_libraries_encode_hires(), test_libraries_encode_lores()

### Community 88 - "base cluster"
Cohesion: 0.24
Nodes (6): PathLike, Path, T, Return the filename for a given camera index., Save all calibration data to disk., Load all calibration data from disk, to be invoked from inheriting class…

### Community 89 - "__init__ cluster"
Cohesion: 0.24
Nodes (7): PluginMediacollectionSpec, Path, UUID, files added to collection. priority modifier allows sync queues to upload…, # list of files that were updated (example, filter applied), deleted a file from collection, share backends shall create a link to the mediaitem ressource so it can be used…

### Community 90 - "gpio cluster"
Cohesion: 0.18
Nodes (6): GroupHardwareInputOutput, BaseModel, AppConfig class providing central config, Configure hardware GPIO, keyboard and more. Find integration information in the…, Button, ZeroButton

### Community 92 - "printer cluster"
Cohesion: 0.33
Nodes (10): classify_linux(), classify_windows(), get_printer_status(), get_printer_status_linux(), get_printer_status_windows(), monitor_printer(), on_state_change(), PrinterStateChange (+2 more)

### Community 93 - "test_multicamera cluster"
Cohesion: 0.38
Nodes (10): patch, Path, TestClient, test_delete_calibration_success(), test_generate_charucoboard_failure(), test_generate_charucoboard_success(), test_get_result_failure(), test_get_result_success() (+2 more)

### Community 94 - "misc cluster"
Cohesion: 0.29
Nodes (9): le, Query, api_gallery_delete(), api_gallery_delete_all(), api_getitem(), api_getitems(), delete, get (+1 more)

### Community 95 - "media cluster"
Cohesion: 0.42
Nodes (8): head, api_getitems_get(), api_getitems_head(), DimensionTypes, get, UUID, head used for download portal to check if the file is available without…, _serve_media_item()

### Community 96 - "resize_algorithm_test cluster"
Cohesion: 0.33
Nodes (8): parametrize, Resampling, cv2_resize(), pil_resize(), benchmark, Image, test_cv2_resize(), test_pil_resize()

### Community 97 - "image cluster"
Cohesion: 0.31
Nodes (5): RembgModelType, draw_rotated_text(), Image, Draw text at an angle into an image, takes the same arguments as Image.text()…, RemovebgStep

### Community 98 - "__init__ cluster"
Cohesion: 0.22
Nodes (5): PluginManagementSpec, init is run on app initialization. plugins are reinitialized on container…, plugin start is called in last step during container.start, plugin stop is called in first step during container.stop, the information service requests reqular statistics from the plugin to display…

### Community 99 - "__init__ cluster"
Cohesion: 0.22
Nodes (6): PluginMediaprocessingSpec, Enum, Image, via hook the filter pipeline step is called. all hooks will be triggered but…, gather all avail filter provided by plugins, gather all filter to be displayed by plugins

### Community 100 - "offset_image_test cluster"
Cohesion: 0.31
Nodes (8): image_hires_rgb(), benchmark, fixture, Image, recenter_image(), recenter_image_chops(), test_recenter_image(), test_recenter_image_chops()

### Community 101 - "scale_video_test cluster"
Cohesion: 0.33
Nodes (8): ffmpeg_h264_scale(), benchmark, fixture, pyav_h264_scale(), test_ffmpeg_h264_scale(), test_pyav_scale(), thread_type(), threading_number()

### Community 102 - "test_actions cluster"
Cohesion: 0.39
Nodes (8): TestClient, test_chose_1pic(), test_chose_1pic_occupied(), test_chose_1pic_otherexception(), test_chose_animation(), test_chose_collage(), test_chose_multicamera(), test_chose_video()

### Community 103 - "processing cluster"
Cohesion: 0.32
Nodes (3): JobModelType, FrontendNotifierEventHooks, SseEventProcessStateinfo

### Community 104 - "tdd_red_guard cluster"
Cohesion: 0.46
Nodes (7): git(), main(), marker_problem(), Path, Claude Code PreToolUse hook: blocks writes to src/photobooth logic until `uv…, The target may not exist yet (Write of a new file); resolve through the nearest…, resolve_target()

### Community 105 - "encode_video_test cluster"
Cohesion: 0.36
Nodes (7): process_ffmpeg(), process_pyav(), benchmark, fixture, run_around_tests(), test_process_ffmpeg(), test_process_pyav()

### Community 106 - "conftest cluster"
Cohesion: 0.43
Nodes (5): create_db_and_tables(), main(), global_function_setup2(), fixture, session_setup1()

### Community 107 - "media_encode cluster"
Cohesion: 0.71
Nodes (6): encode(), __pil_img_save(), Image, Path, __pyav_gif_save(), __pyav_mp4_save()

### Community 108 - "test_share cluster"
Cohesion: 0.48
Nodes (6): TestClient, test_get_limits_reset(), test_get_limits_reset_error(), test_get_limits_reset_nonexistant_failsilent(), test_get_stats_reset_all(), test_get_stats_reset_all_error()

### Community 109 - "test_information cluster"
Cohesion: 0.53
Nodes (5): TestClient, test_get_limits_reset(), test_get_limits_reset_error(), test_get_stats_reset(), test_get_stats_reset_all_error()

### Community 110 - "test_static cluster"
Cohesion: 0.53
Nodes (5): TestClient, test_private_css(), test_private_css_nonexisting_placeholder(), test_read_web_sharepage(), test_read_web_spa()

### Community 111 - "test_tdd_lib cluster"
Cohesion: 0.50
Nodes (5): classify_changes(), entries: [{"status": "A"|"M"|"D"|"R087"..., "path": ...}] as from `git diff…, entry(), test_edge_classify_groups_each_kind(), test_edge_classify_ignores_deletes_and_pure_renames()

### Community 112 - "filter_pilgram2_test cluster"
Cohesion: 0.40
Nodes (4): filter_algo(), benchmark, fixture, test_pilgram_lores_benchmark()

### Community 113 - "test_enumerate cluster"
Cohesion: 0.60
Nodes (4): TestClient, test_admin_enumerate_files(), test_admin_enumerate_serialports(), test_admin_enumerate_usbcameras()

### Community 114 - "tdd_lib cluster"
Cohesion: 0.50
Nodes (4): parse_junit_failures(), Reads pytest --junitxml. A collection failure (usually a module that does not…, test_edge_junit_collection_failure_is_file_level(), test_error_parse_junit_failures_on_empty_or_invalid_xml()

### Community 116 - "test_debug cluster"
Cohesion: 0.67
Nodes (3): TestClient, test_read_log(), test_read_log_err()

## Knowledge Gaps
- **47 isolated node(s):** `photobooth-app`, `new-task-worktree.sh script`, `ADR-0001 AI workflow port`, `Lessons Learned`, `ADR Template` (+42 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **19 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BaseService` connect `BaseService` to `Information Service`, `Media Collection Service`, `App Config & Acquisition Wiring`, `DB Models & Alembic`, `Container, Schemas & SSE`, `processing cluster`, `Service Container Lifecycle`, `GPIO Pin Handling`, `gpio cluster`, `Processing Event Hooks`, `Processing Service`, `Plugin Manager`, `Acquisition Service`, `Configuration Service`, `GPIO Lights Plugin`, `Logging Service`, `gpio cluster`, `share cluster`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **Why does `AcquisitionService` connect `Acquisition Service` to `BaseService`, `Information Service`, `Acquisition API Tests`, `Media Collection Service`, `App Config & Acquisition Wiring`, `Container, Schemas & SSE`, `repeatedtimer cluster`, `processing cluster`, `image cluster`, `Actions Config Group`, `Processing Event Hooks`, `Processing API`, `Processing Service`, `actions cluster`, `actions cluster`, `actions cluster`, `actions cluster`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Why does `AbstractBackend` connect `Abstract Camera Backend` to `Backend Mode Controller`, `App Config & Acquisition Wiring`, `Picamera2 Backend`, `abstractbackend cluster`, `Virtual Camera Source`, `Wigglecam Backend`, `PyAV Webcam Backend`, `digiCamControl Backend`, `resilientservice cluster`, `Acquisition Service`, `Picamera2 Tests`, `V4L Webcam Backend`, `Gphoto2 Backend`, `Webcam/Virtual Backends`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `AcquisitionService` (e.g. with `BaseService` and `InformationService`) actually correct?**
  _`AcquisitionService` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `AbstractBackend` (e.g. with `StoppableThread` and `DigicamcontrolBackend`) actually correct?**
  _`AbstractBackend` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `JobModelBase` (e.g. with `JobModelAnimation` and `CaptureSet`) actually correct?**
  _`JobModelBase` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `MediacollectionService` (e.g. with `BaseService` and `Button`) actually correct?**
  _`MediacollectionService` has 8 INFERRED edges - model-reasoned connections that need verification._