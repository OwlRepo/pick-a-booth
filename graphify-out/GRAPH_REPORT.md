# Graph Report - .  (2026-10-13)

## Corpus Check
- 355 files · ~101,512 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2711 nodes · 5801 edges · 196 communities (162 shown, 34 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 330 edges (avg confidence: 0.61)
- Token cost: 80,272 input · 0 output

## Community Hubs (Navigation)
- DB Models & Alembic
- Picamera2 Tests
- App Config & Acquisition Wiring
- Background Removal (rembg)
- Admin Files & Enumerate API
- Image/Animation Benchmarks
- TDD Test Repo Fixture
- Image Processing Steps
- Commander Plugin
- Abstract Camera Backend
- Media Collection Service
- Collage/Animation Merge
- Actions Config Group
- Processing Event Hooks
- Processing API
- Backend Mode Controller
- Admin Auth (JWT)
- Container, Schemas & SSE
- Share Config Group
- AI Engineering Agents
- Persona Generator
- Multicamera Steps
- Wigglecam Backend
- Encode Benchmarks
- Acquisition Hookspec
- Rclone Synchronizer
- Information Service
- Picamera2 Backend
- AI Engineering Workflows
- Plugin Hookspecs & Stats
- Virtual Camera Source
- GPIO Pin Handling
- App Factory & Startup
- TDD Name Rules
- WLED Plugin
- Gphoto2 Backend
- Config Admin Tests
- Persona Prompts
- AI Workflow Phase Docs
- PyAV Webcam Backend
- Acquisition Service
- Processing Service
- Service Container Lifecycle
- TDD Lib & Bash Guard
- Plugin Manager
- Media Pipeline Core
- Logging Service
- Share-on-Demand PHP
- resilientservice cluster
- Configuration Service
- TDD Red CLI
- Plugin Hookspecs & Stats
- AI Workflow Phase Docs
- Acquisition API Tests
- Media Pipeline Core
- Service Container Lifecycle
- Plugin Hookspecs & Stats
- Filter API
- simple cluster
- AI Runtime Rules & Templates
- filter_pilgram2 cluster
- baseconfig cluster
- sse_ cluster
- __init__ cluster
- repeatedtimer cluster
- base cluster
- encode_animation_test cluster
- tdd_gate cluster
- multicamera cluster
- charuco_board cluster
- scale_image_test cluster
- stream_lores_test cluster
- test_system cluster
- __init__ cluster
- Admin Auth (JWT)
- digiCamControl Backend
- BaseService
- gpio cluster
- test_filter cluster
- video cluster
- simple cluster
- resilientservice cluster
- misc cluster
- GPIO Lights Plugin
- crop_image_test cluster
- AI Workflow Phase Docs
- base cluster
- BaseService
- __init__ cluster
- Plugin Hookspecs & Stats
- Acquisition API
- abstractbackend cluster
- gpio cluster
- share cluster
- printer cluster
- test_multicamera cluster
- AI Workflow Phase Docs
- misc cluster
- image cluster
- Plugin Hookspecs & Stats
- test_actions cluster
- Media Collection Service
- media cluster
- resize_algorithm_test cluster
- WLED Config
- offset_image_test cluster
- scale_video_test cluster
- WLED Config
- Container, Schemas & SSE
- project-memory cluster
- processing cluster
- tdd_red_guard cluster
- Acquisition API
- Admin Files & Enumerate API
- encode_video_test cluster
- AI Engineering Workflows
- Persona Prompts
- multicamera cluster
- media_encode cluster
- test_share cluster
- AI Engineering Workflows
- Plugin Hookspecs & Stats
- conftest cluster
- App Factory & Startup
- test_information cluster
- test_static cluster
- AI Workflow Phase Docs
- test_tdd_lib cluster
- base_plugin cluster
- App Factory & Startup
- App Factory & Startup
- misc cluster
- misc cluster
- filter_pilgram2_test cluster
- test_enumerate cluster
- tdd_lib cluster
- GPIO Lights Plugin
- test_debug cluster
- project-memory cluster
- CONTRIBUTING cluster
- Webcam/Virtual Backends
- Persona Prompts
- Acquisition Service
- Image Processing Steps
- Persona Prompts
- AI Runtime Rules & Templates
- eod-report cluster
- project-memory cluster
- AI Workflow Phase Docs
- new-task-worktree cluster
- __init__ cluster
- Acquisition Service
- Acquisition Service
- Acquisition Service
- __init__ cluster
- __init__ cluster
- Acquisition Service
- AI Engineering Workflows
- bug_report cluster
- feature_request cluster
- AI Engineering Workflows
- Persona Prompts
- Persona Prompts
- Persona Prompts
- Persona Prompts
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
9. `BaseSession` - 33 edges
10. `ImageContext` - 32 edges

## Surprising Connections (you probably didn't know these)
- `Strict TDD` --semantically_similar_to--> `Strict TDD (principle 6b)`  [INFERRED] [semantically similar]
  docs/ai/testing-strategy.md → AGENTS.md
- `Worktree and branch isolation` --semantically_similar_to--> `Task worktree isolation`  [INFERRED] [semantically similar]
  docs/ai/execution.md → AGENTS.md
- `Dispatch Round Structure` --semantically_similar_to--> `Contract-First Dispatch`  [INFERRED] [semantically similar]
  docs/ai/agent-orchestration.md → agents/src/prompts/project-manager.md
- `test_edge_find_bash_write_targets_detects_writes()` --calls--> `find_bash_write_targets()`  [INFERRED]
  scripts/tests/test_tdd_lib.py → scripts/ci/tdd_lib.py
- `README.md photobooth-app` --references--> `LICENSE.md (MIT)`  [INFERRED]
  README.md → LICENSE.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Canonical flow mandatory doc loads** — agents_canonical_task_flow, docs_ai_plan_template, docs_ai_execution, docs_ai_testing_strategy, docs_ai_autonomous_engineering [EXTRACTED 0.90]
- **Contract-first multi-agent dispatch** — agents_src_prompts_project_manager_contract_first_dispatch, docs_ai_agent_orchestration_dispatch_round_structure, docs_ai_agent_orchestration_file_ownership_rule, docs_ai_agent_orchestration_round_1b_red, docs_ai_agent_orchestration_round_4_qa_fan_out [INFERRED 0.85]
- **Strict TDD enforcement system** — docs_ai_testing_strategy_strict_tdd, docs_ai_testing_strategy_tdd_enforcement_hook_ci_gate, docs_ai_testing_strategy_tdd_lib_classification_guarded_logic, agents_strict_tdd_principle_6b, docs_ai_agent_orchestration_round_1b_red [INFERRED 0.80]
- **Agent role contracts** — ai_engineering_agents_product_manager, ai_engineering_agents_architect, ai_engineering_agents_coordinator, ai_engineering_agents_implementer, ai_engineering_agents_reviewer, ai_engineering_agents_qa, ai_engineering_agents_reporter [EXTRACTED 1.00]
- **Task lifecycle state docs** — ai_engineering_core_task_lifecycle, ai_engineering_core_task_state_machine, ai_engineering_core_task_state_machine_skipped_already_implemented, ai_engineering_core_task_state_machine_blocked_states, ai_engineering_core_task_state_machine_waiting_approval [INFERRED 0.85]
- **Report templates** — ai_engineering_templates_execution_report_doc, ai_engineering_templates_review_report_doc, ai_engineering_templates_qa_report_doc, ai_engineering_templates_pr_report_doc, ai_engineering_templates_eod_report_doc [INFERRED 0.75]
- **Phase-loaded AI workflow workflow docs** — _ai_engineering_workflows_task_intake, _ai_engineering_workflows_feature_development, _ai_engineering_workflows_review_process, _ai_engineering_workflows_release_process, _ai_engineering_workflows_bug_fix, _ai_engineering_workflows_blocker_handling, _ai_engineering_workflows_daily_cycle [INFERRED 0.85]
- **GitHub Actions CI workflows** — _github_workflows_ai_gates, _github_workflows_benchmarks, _github_workflows_cicd, _github_workflows_linter, _github_workflows_pytests [INFERRED 0.85]
- **Canonical task flow phase docs** — docs_ai_planning, docs_ai_execution, docs_ai_handoff, docs_ai_task_router [EXTRACTED 0.95]
- **Plan prompt templates** — docs_ai_prompts_bugfix_rca, docs_ai_prompts_bugfix_plan, docs_ai_prompts_feature_plan, docs_ai_prompts_refactor_plan [EXTRACTED 0.90]

## Communities (196 total, 34 thin omitted)

### Community 0 - "DB Models & Alembic"
Cohesion: 0.05
Nodes (30): datetime, DeclarativeBase, listens_for, AppConfig class providing central config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online() (+22 more)

### Community 1 - "Picamera2 Tests"
Cohesion: 0.05
Nodes (46): HTTPServer, Convert JPG/MJPG and YUVY pixelformat to output JPG, WebcamV4lBackend, BaseModelCamera, GroupBackend, GroupCameraDigicamcontrol, GroupCameraGphoto2, GroupCameraPicamera2 (+38 more)

### Community 2 - "App Config & Acquisition Wiring"
Cohesion: 0.07
Nodes (21): manage up to two photobooth-app backends in this module, FrameOverlay, BaseModel, UUID, JobModelAnimation, Event, JobModelCollage, Event (+13 more)

### Community 3 - "Background Removal (rembg)"
Cohesion: 0.06
Nodes (36): SessionOptions, naive_cutout(), Any, PILImage, The util is very much inspired by https://github.com/danielgatis/rembg Thank…, Remove the background from an input image., remove(), new_session() (+28 more)

### Community 4 - "Admin Files & Enumerate API"
Cohesion: 0.06
Nodes (53): Body, api_get_rclone_remotes(), api_get_serial_ports(), api_get_usbcameras(), get_search(), get, api_clearrecycledir(), create_upload_file() (+45 more)

### Community 5 - "Image/Animation Benchmarks"
Cohesion: 0.06
Nodes (48): BytesIO, benchmark, test_transpose_piexif(), test_transpose_pillow(), transpose_piexif(), transpose_pillow(), ffmpeg_hq_optimizedquality_scale(), ffmpeg_hq_optimizedspeed_scale() (+40 more)

### Community 6 - "TDD Test Repo Fixture"
Cohesion: 0.10
Nodes (50): git(), make_repo(), Path, Repo, run_script(), write(), cited_paths(), Path (+42 more)

### Community 7 - "Image Processing Steps"
Cohesion: 0.11
Nodes (43): Color, PluginFilters, TextsConfig, ImageContext, process_image_inner(), Unified handling of images that are just one single capture: 1pictaken…, FillBackgroundStep, get_plugin_avail_filters() (+35 more)

### Community 8 - "Commander Plugin"
Cohesion: 0.11
Nodes (31): eventHooks, field_validator, Commander, Event, hookimpl, MediaitemTypes, State, ThreadCommand (+23 more)

### Community 9 - "Abstract Camera Backend"
Cohesion: 0.07
Nodes (25): AbstractBackend, BackendStats, LoresBroadcastRes, MulticamRequest, ABC, Orientation, # TODO: validate 0.5 tolerance., defines some common stats - if backend supports, they return these properties,… (+17 more)

### Community 10 - "Media Collection Service"
Cohesion: 0.07
Nodes (37): MediacollectionService, UUID, Handle all image related stuff, client(), client_authenticated(), global_function_setup1(), global_function_setup2(), fixture (+29 more)

### Community 11 - "Collage/Animation Merge"
Cohesion: 0.11
Nodes (28): AnimationMergeDefinition, CollageMergeDefinition, BaseModel, AnimationContext, CollageContext, PipelineStep, process_and_generate_animation(), process_and_generate_collage() (+20 more)

### Community 12 - "Actions Config Group"
Cohesion: 0.08
Nodes (32): api_applyfilter(), api_get_preview_image_filtered(), api_get_userselectable_filters(), get, patch, UUID, AnimationConfigurationSet, AnimationProcessing (+24 more)

### Community 13 - "Processing Event Hooks"
Cohesion: 0.06
Nodes (16): DbListenter, PluginEventHooks, Event, State, JobModelBase, ABC, Event, UUID (+8 more)

### Community 14 - "Processing API"
Cohesion: 0.07
Nodes (27): BackgroundTasks, deprecated, api_cmd_abort_get(), api_cmd_confirm_get(), api_cmd_reject_get(), api_get_preview_image_filtered(), get, UUID (+19 more)

### Community 15 - "Backend Mode Controller"
Cohesion: 0.07
Nodes (17): Modes, ModeController, Path, Einfacher Mode-Controller mit: - requested_mode (Thread-agnostisch) -…, usually requested when creating a video but also for livestream. livestream…, Monitor thread function to request standby if no livestream is requested for…, Wird im stream-thread aufgerufen, wenn es passend für einen potentiellen mode-…, called during device setup (+9 more)

### Community 16 - "Admin Auth (JWT)"
Cohesion: 0.12
Nodes (31): oauth2_scheme, OAuth2PasswordRequestForm, login_for_access_token(), Depends, get, post, read_users_me(), authenticate_user() (+23 more)

### Community 17 - "Container, Schemas & SSE"
Cohesion: 0.09
Nodes (14): MediaitemPublic, BaseModel, ShareLimitsPublic, UsageStatsPublic, BaseModel, # FIXME: workaround for testing until testing with mocks/patching works well..., basic class for sse events, SseEventBase (+6 more)

### Community 18 - "Share Config Group"
Cohesion: 0.12
Nodes (29): GroupShare, BaseModel, AppConfig class providing central config, Configure share or print actions., Configure additional parameter for the share command to input by the user., Configure options to share or print images., Configure stages how to process mediaitem before printing on paper., ShareConfigurationSet (+21 more)

### Community 19 - "AI Engineering Agents"
Cohesion: 0.10
Nodes (28): architect, coordinator, implementer, product-manager, qa, reporter, reviewer, PILOT_FROZEN activation (+20 more)

### Community 20 - "Persona Generator"
Cohesion: 0.13
Nodes (24): Persona, check(), claude_file(), compute_targets(), _escape(), find_duplicate_owned_globs(), generate(), load_personas() (+16 more)

### Community 21 - "Multicamera Steps"
Cohesion: 0.13
Nodes (16): MatLike, MulticameraContext, AutoPivotPointStep, CropCommonAreaStep, OffsetPerOpticalFlowStep, Image, NextStep, Draw a bounding box on a copy of the image. box = (x_min, y_min, x_max, y_max)… (+8 more)

### Community 22 - "Wigglecam Backend"
Cohesion: 0.13
Nodes (11): Path, Trigger a capture request and collect hi-res images from all cameras., Background loop to receive lores frames., WigglecamBackend, GroupCameraWigglecam, WigglecamNodes, backend_wigglecam(), fixture (+3 more)

### Community 23 - "Encode Benchmarks"
Cohesion: 0.13
Nodes (22): cv2_encode_jpg(), cv2_encode_png_lossless(), cv2_encode_webp(), image(), image_hires(), image_lores(), library(), library_yuv420() (+14 more)

### Community 24 - "Acquisition Hookspec"
Cohesion: 0.12
Nodes (14): hookspec, PluginAcquisitionSpec, PluginMediaprocessingSpec, Enum, Image, via hook the filter pipeline step is called. all hooks will be triggered but…, gather all avail filter provided by plugins, gather all filter to be displayed by plugins (+6 more)

### Community 25 - "Rclone Synchronizer"
Cohesion: 0.11
Nodes (15): UUID, https://photobooth-app.org/setup/configuration/qrshareservice/, setup the resource right before run_service logic, tear down the resource right after run_service logic and in case of crashes, service logic to be run when the service is started, ShareOnDemandService, _mediaitem(), fixture (+7 more)

### Community 26 - "Information Service"
Cohesion: 0.13
Nodes (3): InformationService, Any, Raspberry Pi system health monitor using vcgencmd. Decode throttled bitmask…

### Community 27 - "Picamera2 Backend"
Cohesion: 0.11
Nodes (6): Picamera2Backend, Path, Every camera tuning file usually has at least "normal", "short" and "long"…, function that returns None if value is None, otherwise round is applied and…, picamera2 has local start_recording, which overrides the abstract class…, on start set autofocus to continuous if requested by config or auto and trigger…

### Community 28 - "AI Engineering Workflows"
Cohesion: 0.11
Nodes (19): Autonomous Engineering Layer (.ai-engineering), autonomous-engineering.yaml config, doc link test (test_doc_links.py), Activation states PILOT_FROZEN/ACTIVE/RELEASE_FROZEN, Bootstrap validation workflow, Blocker Handling workflow, Task Intake workflow, Caveman ultra policy (+11 more)

### Community 29 - "Plugin Hookspecs & Stats"
Cohesion: 0.20
Nodes (11): PipelineStats, PrioritizedJob, ThreadedImmediateSyncPipeline, CopyOperation, DeleteOperation, JobResult, JobStatus, Enum (+3 more)

### Community 30 - "Virtual Camera Source"
Cohesion: 0.13
Nodes (4): Path, for other threads to receive a hq JPEG image, VirtualCameraBackend, test_optimize_mode()

### Community 31 - "GPIO Pin Handling"
Cohesion: 0.15
Nodes (15): PinHandler, gpio_service(), pinhandler1(), fixture, patch, test_action_buttons(), test_button_reboot(), test_button_share() (+7 more)

### Community 32 - "App Factory & Startup"
Cohesion: 0.13
Nodes (13): FastAPI, _create_app(), lifespan(), api_trigger_model(), ActionType, get, Example 2nd-level subpackage., api_get_config_current_active() (+5 more)

### Community 33 - "TDD Name Rules"
Cohesion: 0.15
Nodes (22): check_names(), extract_test_names(), judge_red(), parse_waivers(), added: names introduced by the diff (any file). new_files: full ordered names…, Test functions pytest would collect, in declaration order. Strings, comments…, added(), test_edge_extract_handles_async_methods_and_skips_fixtures() (+14 more)

### Community 34 - "WLED Plugin"
Cohesion: 0.17
Nodes (5): hookimpl, State, To start the resilient service, To stop the resilient service, Wled

### Community 35 - "Gphoto2 Backend"
Cohesion: 0.13
Nodes (7): Gphoto2Backend, Gphoto2Parameters, Configure different settings when switching between modes., backend_gphoto2(), fixture, run_around_tests(), test_get_gphoto2_switch_modes()

### Community 36 - "Config Admin Tests"
Cohesion: 0.14
Nodes (19): AppConfig, AppConfig class glueing all together In the case where a value is specified for…, patch, TestClient, test_config_endpoints_ui(), test_config_getschema(), test_config_patch(), test_config_post_validationerror() (+11 more)

### Community 37 - "Persona Prompts"
Cohesion: 0.10
Nodes (19): ADR-0001 AI workflow port, ADR-0002 Claude Code only runtime, Automatic agent routing default, Contract-First Dispatch, project-manager persona, accessibility-auditor persona, code-reviewer persona, db-architect persona (+11 more)

### Community 38 - "AI Workflow Phase Docs"
Cohesion: 0.16
Nodes (9): Maps are not proof; code wins, Completion Gate, Integration sequence, Plan template skeleton, Test Matrix, Graphify discovery first, Unauthenticated api surface risk, Task classification routing (+1 more)

### Community 39 - "PyAV Webcam Backend"
Cohesion: 0.12
Nodes (7): InputContainer, Packet, WebcamPyavBackend, PermanentFault, Raised from within the services when the service should not attempt recovery., test_optimize_mode(), VideoStream

### Community 40 - "Acquisition Service"
Cohesion: 0.14
Nodes (12): AcquisitionService, _acqs(), fixture, get video from service, test_get_livestream_virtualcamera(), test_get_multicam_files(), test_getimage(), test_getimages_directlyaccess_backends() (+4 more)

### Community 41 - "Processing Service"
Cohesion: 0.13
Nodes (6): ProcessingService, ActionType, if queue is initialized on _external_cmd_queue, a user request is waited for., some visible message in frontend, SseEventTranslateableFrontendNotification, userEvents

### Community 42 - "Service Container Lifecycle"
Cohesion: 0.18
Nodes (10): DigitalOutputDevice, Events, GpioLight, GpioLightsConfig, BaseModel, AppDigitalOutputDevice, GpioLights, Event (+2 more)

### Community 43 - "TDD Lib & Bash Guard"
Cohesion: 0.13
Nodes (20): expr, find_bash_write_targets(), _is_fixture(), is_guarded_source(), _is_path_arg(), kind_of(), NamedTuple, Shared rules for the TDD gate (CI), `uv run poe tdd:red` (local) and the Claude… (+12 more)

### Community 44 - "Plugin Manager"
Cohesion: 0.15
Nodes (7): BasePlugin, PluginManagerService, When the pluginmanager is started, it will start all registered plugins that…, When the pluginmanager is stoppped, it will stop all registered plugins that…, pluginmanager_service(), fixture, test_list_plugins()

### Community 45 - "Media Pipeline Core"
Cohesion: 0.22
Nodes (12): VideoContext, BoomerangStep, LoopStep, NextStep, benchmark, test_encode_boomerang_pyav(), test_loop_pyav(), video_boomerangPyav_stage() (+4 more)

### Community 46 - "Logging Service"
Cohesion: 0.13
Nodes (7): ExceptHookArgs, LogRecord, ConsoleColorFormatter, EventstreamLogHandler, LoggingService, mute some logger by rasing their log level, Logging handler to emit events to eventstream; to be displayed in console.log…

### Community 47 - "Share-on-Demand PHP"
Cohesion: 0.22
Nodes (3): RuntimeException, AuthException, ShareService

### Community 48 - "resilientservice cluster"
Cohesion: 0.17
Nodes (10): RcloneApi, CrashReporter, ABC, Exception, QuietCrashReporter, Raised when the service probably only crashes temporarily and there is a chance…, Raised when the service probably crashes permanently and will do so after a…, ServiceCrashedPermanently (+2 more)

### Community 49 - "Configuration Service"
Cohesion: 0.18
Nodes (7): ConfigurationService, Any, AnyStr, configuration_service(), fixture, test_plugin_config_get_current(), test_plugin_config_get_schema()

### Community 50 - "TDD Red CLI"
Cohesion: 0.22
Nodes (15): changed_entries(), git(), main(), parse_args(), Exception, Path, `uv run poe tdd:red`: run this branch's changed tests BEFORE implementing and…, Committed + staged + unstaged changes against the merge-base, plus untracked… (+7 more)

### Community 51 - "Plugin Hookspecs & Stats"
Cohesion: 0.18
Nodes (8): SubList, SubStats, RcloneApi, Returns set of removable drives detected on the computer., Stats, ThreadedRegularSync, get_corresponding_remote_file(), Path

### Community 52 - "AI Workflow Phase Docs"
Cohesion: 0.15
Nodes (15): Canonical Task Flow, Graphify discovery, Task worktree isolation, How agents operate (PR flow), Origin freshness and app-managed worktrees, Implementation rules, Mandatory Graphify closeout, QA mode (+7 more)

### Community 53 - "Acquisition API Tests"
Cohesion: 0.26
Nodes (15): asyncio, capture(), patch, TestClient, test_aquire_multiple_nomodechange(), test_aquire_multiple_withmodechange(), test_aquire_still_capturemode(), test_aquire_still_exception() (+7 more)

### Community 54 - "Media Pipeline Core"
Cohesion: 0.16
Nodes (9): Context, ErrorHandler, _default_error_handler(), Pipeline, PipelineCursor, PipelineError, Any, Exception (+1 more)

### Community 55 - "Service Container Lifecycle"
Cohesion: 0.24
Nodes (9): Container, stop all services first (reverse order), then start them again., test_hooks_integration_start_stop_if_hook_implemented(), _container(), fixture, test_hooks_integration(), test_light_switched_during_process(), test_light_switched_during_process_turn_off_after_capture() (+1 more)

### Community 56 - "Plugin Hookspecs & Stats"
Cohesion: 0.22
Nodes (11): SynchronizerConfig, Synchronizer, fixture, Create a SynchronizerRclone with mocked config + mocked rclone client., sync(), test_collection_hooks(), test_copy_sharepage_to_remotes(), test_get_share_links_public() (+3 more)

### Community 57 - "Filter API"
Cohesion: 0.19
Nodes (10): api_get_calibration_stats(), api_get_result(), get, MulticameraProcessing, process_and_generate_wigglegram(), process_video(), process_wigglegram_inner(), Image (+2 more)

### Community 58 - "simple cluster"
Cohesion: 0.18
Nodes (9): api_delete_calibration_delete(), delete, Image, Reset calibration data., Compute the common overlapping crop region across all cameras. Returns (x1, y1,…, Specialized calibration manager., Crop a Pillow image to the given rectangle. Args: img (Image.Image): Input PIL…, align all images, while 1 image per camera, sorted by the index (+1 more)

### Community 59 - "AI Runtime Rules & Templates"
Cohesion: 0.14
Nodes (15): ADR Template, Execution Report Template, docs/ai/plan-template.md, Plan Template (short form), QA Report Template, Review Report Template, uv run poe agents:lint, Agent Contract Validation (+7 more)

### Community 60 - "filter_pilgram2 cluster"
Cohesion: 0.25
Nodes (7): available_filter, FilterPilgram2Config, FilterPilgram2, hookimpl, Image, filter_pilgram2_plugin(), fixture

### Community 61 - "baseconfig cluster"
Cohesion: 0.16
Nodes (6): BaseSettings, PydanticBaseSettingsSource, BaseConfig, Remove allof that would interfere with the normal processing of jsonforms…, Get schema to build UI. Schema is polished to the needs of UI, Persist config to file

### Community 62 - "sse_ cluster"
Cohesion: 0.16
Nodes (8): Request, get, Eventstream to feed clients with server generated events and data, subscribe(), class providing central sse, Client, Class each individual client connected, SseService

### Community 63 - "__init__ cluster"
Cohesion: 0.15
Nodes (9): DisplayEnum, GenericStats, StrEnum, PluginManagementSpec, class providing central plugin repo, init is run on app initialization. plugins are reinitialized on container…, plugin start is called in last step during container.start, plugin stop is called in first step during container.stop (+1 more)

### Community 64 - "repeatedtimer cluster"
Cohesion: 0.16
Nodes (6): Repeat Timer in separate thread for tasks to be executed in intervals, Call a function after a specified number of seconds: t = Timer(30.0, f,…, Stop the timer if it hasn't finished yet., RepeatedTimer, Timer, Thread

### Community 65 - "base cluster"
Cohesion: 0.21
Nodes (7): CalibrationBase, Path, T, Base class providing save/load functionality for calibration data., Return the filename for a given camera index., Save all calibration data to disk., Load all calibration data from disk, to be invoked from inheriting class…

### Community 66 - "encode_animation_test cluster"
Cohesion: 0.21
Nodes (14): dummy_images(), library(), pillow_encode_avif(), pillow_encode_gif(), pillow_encode_webp(), Any, benchmark, fixture (+6 more)

### Community 67 - "tdd_gate cluster"
Cohesion: 0.31
Nodes (13): changed_entries(), collect_names(), GateError, git(), main(), Exception, CI TDD gate for pull requests. Rules: docs/ai/testing-strategy.md "Strict TDD".…, Runs the PR's test files against the merge-base source in a throwaway worktree. (+5 more)

### Community 69 - "charuco_board cluster"
Cohesion: 0.25
Nodes (12): generate_board(), get_detector(), CharucoDetector, ndarray, Size: (SquaresX, SquaresY), while X is left-right (width/columns) and Y top-…, Size: (SquaresX/Cols, SquaresY/Rows), while X is left-right and Y is top-bottom, dummy_charuco_images(), fixture (+4 more)

### Community 70 - "scale_image_test cluster"
Cohesion: 0.24
Nodes (13): cv2_scale(), image(), image_hires(), image_lores(), library(), pillow_scale(), benchmark, fixture (+5 more)

### Community 71 - "stream_lores_test cluster"
Cohesion: 0.26
Nodes (13): benchmark, pyav_cv2_scale(), pyav_pillow_scale(), pyav_scale_cv2_encode(), pyav_scale_simplejpeg_encode(), pyav_simplejpeg_scale(), pyav_turbojpeg_scale(), test_pyav_cv2_scale() (+5 more)

### Community 72 - "test_system cluster"
Cohesion: 0.24
Nodes (13): fixture, patch, TestClient, system_host_endpoint(), system_nonexistant_endpoint(), system_service_endpoint(), system_systemctl_endpoint(), system_systemctl_installuninstall_endpoint() (+5 more)

### Community 73 - "__init__ cluster"
Cohesion: 0.32
Nodes (8): PluginStatemachineSpec, Event, MediaitemTypes, State, job processor before a transition takes place. for details see python…, job processor when exit a state. for details see python statemachine library, job processor when the new state is entered. for details see python…, job processor after a transition took place. for details see python…

### Community 74 - "Admin Auth (JWT)"
Cohesion: 0.19
Nodes (12): api_get_config_current_active(), api_get_config_schema(), api_get_configurables(), api_post_config_current(), api_reset_all_config(), api_reset_config(), Any, AnyStr (+4 more)

### Community 75 - "digiCamControl Backend"
Cohesion: 0.17
Nodes (3): DigicamcontrolBackend, r""" Digicamcontrol backend implementation Quirks: - using webfrontend only…, test_optimize_mode()

### Community 76 - "BaseService"
Cohesion: 0.24
Nodes (4): BaseService, EnumStatus, Enum, All services (factory/singleton) and resources derive from this base class…

### Community 78 - "test_filter cluster"
Cohesion: 0.26
Nodes (11): Example 2nd-level subpackage., TestClient, test_apply_filter(), test_apply_filter_nonexistentfilter(), test_get_avail_filter(), test_get_avail_filter_err(), test_preview_filter_1977(), test_preview_filter_nonexistentfilter() (+3 more)

### Community 80 - "simple cluster"
Cohesion: 0.23
Nodes (8): CharucoDetector, ndarray, Path, Aggregate detections from multiple images of the same camera. Returns stacked…, Compute homography between reference and current camera using common ChArUco…, Calibrate one camera against the reference and save homography., Load all calibration data from disk., Calibrate all cameras against the reference camera. cameras[0] is all images…

### Community 81 - "resilientservice cluster"
Cohesion: 0.21
Nodes (4): setup the resource right before run_service logic, tear down the resource right after run_service logic and in case of crashes, service logic to be run when the service is started, ResilientService

### Community 82 - "misc cluster"
Cohesion: 0.20
Nodes (9): field_serializer, GroupCommon, BaseModel, SerializationInfo, AppConfig class providing central config, Common config for photobooth., contextual_serializer_password(), Any (+1 more)

### Community 83 - "GPIO Lights Plugin"
Cohesion: 0.20
Nodes (8): api_get_statscounter_reset_all(), api_get_statscounter_reset_field(), get, api_get_limitscounter_reset_all(), api_get_limitscounter_reset_field(), get, TestClient, test_sse_stream1()

### Community 84 - "crop_image_test cluster"
Cohesion: 0.24
Nodes (8): image(), image_hires(), image_lores(), library(), benchmark, fixture, test_libraries_encode_hires(), test_libraries_encode_lores()

### Community 85 - "AI Workflow Phase Docs"
Cohesion: 0.27
Nodes (10): Core principles, Strict TDD (principle 6b), Round 1b RED, Backend Five-Bucket Sweep, Known limits of TDD gate, Live verification (front and back), Mandatory Test Layers, Strict TDD (+2 more)

### Community 86 - "base cluster"
Cohesion: 0.27
Nodes (6): PathLike, CalibrationDataExtrinsics, CalibrationDataIntrinsics, PersistableDataclass, CalDataAlign, Set identity caldata so output will not be modified at all but useful in testing

### Community 87 - "BaseService"
Cohesion: 0.22
Nodes (3): skipif, SystemService, test_systemd_control()

### Community 88 - "__init__ cluster"
Cohesion: 0.24
Nodes (7): PluginMediacollectionSpec, Path, UUID, files added to collection. priority modifier allows sync queues to upload…, # list of files that were updated (example, filter applied), deleted a file from collection, share backends shall create a link to the mediaitem ressource so it can be used…

### Community 89 - "Plugin Hookspecs & Stats"
Cohesion: 0.29
Nodes (9): Common, OndemandShareConfig, BaseModel, RcloneConfig, RemoteConfig, ShareConfig, RcloneApi, test_immediateSnycPipeline_skip_delete_op_when_upload_only_is_enabled() (+1 more)

### Community 90 - "Acquisition API"
Cohesion: 0.27
Nodes (10): api_cmd_aquisition_capturemode_get(), api_multicam_get(), api_multicam_loadfile_get(), api_still_get(), get, Path, set backends to preview or capture mode (usually automatically switched as…, video_stream() (+2 more)

### Community 91 - "abstractbackend cluster"
Cohesion: 0.22
Nodes (5): Framerate, public api, non-blocking, call by backends implementation when frame is delivered, so the fps can be…, Thread-safe rolling-window FPS calculator., Return remaining nanoseconds until the next frame should be processed. Positive…

### Community 92 - "gpio cluster"
Cohesion: 0.22
Nodes (7): GroupHardwareInputOutput, BaseModel, AppConfig class providing central config, Configure hardware GPIO, keyboard and more. Find integration information in the…, Button, submit events on gpio pin interrups Pin Numbering:…, ZeroButton

### Community 94 - "printer cluster"
Cohesion: 0.33
Nodes (10): classify_linux(), classify_windows(), get_printer_status(), get_printer_status_linux(), get_printer_status_windows(), monitor_printer(), on_state_change(), PrinterStateChange (+2 more)

### Community 95 - "test_multicamera cluster"
Cohesion: 0.38
Nodes (10): patch, Path, TestClient, test_delete_calibration_success(), test_generate_charucoboard_failure(), test_generate_charucoboard_success(), test_get_result_failure(), test_get_result_success() (+2 more)

### Community 96 - "AI Workflow Phase Docs"
Cohesion: 0.20
Nodes (9): Config and runtime rules, Database rules (additive migrations), Don't rules, Layers (routers services backends plugins database), pick-a-booth project context, Public fork of photobooth-app, Tech stack (Python FastAPI uv SQLite), Maintenance Rules (CONTEXT DRIFT) (+1 more)

### Community 97 - "misc cluster"
Cohesion: 0.29
Nodes (9): le, Query, api_gallery_delete(), api_gallery_delete_all(), api_getitem(), api_getitems(), delete, get (+1 more)

### Community 98 - "image cluster"
Cohesion: 0.27
Nodes (6): RembgModelType, draw_rotated_text(), Image, Draw text at an angle into an image, takes the same arguments as Image.text()…, RemovebgStep, test_rembg_ai_stage()

### Community 99 - "Plugin Hookspecs & Stats"
Cohesion: 0.31
Nodes (3): hookimpl, Path, UUID

### Community 100 - "test_actions cluster"
Cohesion: 0.36
Nodes (9): ProcessMachineOccupiedError, TestClient, test_chose_1pic(), test_chose_1pic_occupied(), test_chose_1pic_otherexception(), test_chose_animation(), test_chose_collage(), test_chose_multicamera() (+1 more)

### Community 101 - "Media Collection Service"
Cohesion: 0.36
Nodes (9): patch, TestClient, test_delete_item(), test_delete_items(), test_delete_items_exception(), test_get_item(), test_get_item_exception(), test_get_items() (+1 more)

### Community 102 - "media cluster"
Cohesion: 0.42
Nodes (8): head, api_getitems_get(), api_getitems_head(), DimensionTypes, get, UUID, head used for download portal to check if the file is available without…, _serve_media_item()

### Community 103 - "resize_algorithm_test cluster"
Cohesion: 0.33
Nodes (8): parametrize, Resampling, cv2_resize(), pil_resize(), benchmark, Image, test_cv2_resize(), test_pil_resize()

### Community 104 - "WLED Config"
Cohesion: 0.31
Nodes (6): Common, BaseModel, WledConfig, Enum, Event, WledPreset

### Community 105 - "offset_image_test cluster"
Cohesion: 0.31
Nodes (8): image_hires_rgb(), benchmark, fixture, Image, recenter_image(), recenter_image_chops(), test_recenter_image(), test_recenter_image_chops()

### Community 106 - "scale_video_test cluster"
Cohesion: 0.33
Nodes (8): ffmpeg_h264_scale(), benchmark, fixture, pyav_h264_scale(), test_ffmpeg_h264_scale(), test_pyav_scale(), thread_type(), threading_number()

### Community 107 - "WLED Config"
Cohesion: 0.28
Nodes (8): fixture, should just fail in silence if disabled but app triggers some presets, test_change_presets(), test_disabled(), test_enabled_emptyport(), test_enabled_nonexistentserialport(), test_restart_class(), wled_plugin()

### Community 108 - "Container, Schemas & SSE"
Cohesion: 0.33
Nodes (8): _container(), fixture, Testing exceptions in backends, container reloading works reliable, container start services do not re-raise exceptions again if during start/stop…, test_container_reload(), test_service_start_exceptions(), test_service_stop_exceptions()

### Community 109 - "project-memory cluster"
Cohesion: 0.32
Nodes (8): Lessons Learned, Project Memory, PILOT_FROZEN activation state, config/autonomous-engineering.yaml, Scheduler Rules, docs/ai/autonomous-engineering.md, Work Orders (Tasks.md), Task Template

### Community 110 - "processing cluster"
Cohesion: 0.32
Nodes (3): JobModelType, FrontendNotifierEventHooks, SseEventProcessStateinfo

### Community 111 - "tdd_red_guard cluster"
Cohesion: 0.46
Nodes (7): git(), main(), marker_problem(), Path, Claude Code PreToolUse hook: blocks writes to src/photobooth logic until `uv…, The target may not exist yet (Write of a new file); resolve through the nearest…, resolve_target()

### Community 112 - "Acquisition API"
Cohesion: 0.43
Nodes (7): api_download_item_id_get_sharelinks(), api_share_item_id(), api_share_latest(), get, post, UUID, _share()

### Community 113 - "Admin Files & Enumerate API"
Cohesion: 0.36
Nodes (7): api_get_userfiles(), get, TestClient, test_get(), test_get_404_missing_item(), test_get_500_on_illegal(), test_get_file_from_demofolder()

### Community 114 - "encode_video_test cluster"
Cohesion: 0.36
Nodes (7): process_ffmpeg(), process_pyav(), benchmark, fixture, run_around_tests(), test_process_ffmpeg(), test_process_pyav()

### Community 115 - "AI Engineering Workflows"
Cohesion: 0.33
Nodes (7): Daily Cycle workflow, Feature Development workflow, Release Process workflow, Review Process workflow, Agent roles (PM, Architect, Coordinator, Implementer, Reviewer, QA, Reporter), Human approval gate (WAITING_APPROVAL, PILOT_FROZEN), Task state machine (NEW to REPORTED)

### Community 116 - "Persona Prompts"
Cohesion: 0.29
Nodes (7): fastapi-backend-dev persona prompt, security-auditor persona prompt, web-frontend-dev persona prompt, API auth model (/api open, /api/admin JWT), architecture-manifest doc, context-refresh doc, api-contracts doc

### Community 118 - "multicamera cluster"
Cohesion: 0.33
Nodes (7): api_get_calibration_generate_charucoboard(), api_post_calibrate_all(), CalibrationRequest, CharucoBoardDefinition, BaseModel, post, Post files to calculate a new calibration, save it and reload services to apply…

### Community 119 - "media_encode cluster"
Cohesion: 0.71
Nodes (6): encode(), __pil_img_save(), Image, Path, __pyav_gif_save(), __pyav_mp4_save()

### Community 120 - "test_share cluster"
Cohesion: 0.48
Nodes (6): TestClient, test_get_limits_reset(), test_get_limits_reset_error(), test_get_limits_reset_nonexistant_failsilent(), test_get_stats_reset_all(), test_get_stats_reset_all_error()

### Community 121 - "AI Engineering Workflows"
Cohesion: 0.33
Nodes (6): Dependabot config (pip + github-actions, target dev), Pull request template, ai-gates CI workflow, benchmarks CI workflow, lint CI workflow, tests CI workflow (Python matrix)

### Community 123 - "conftest cluster"
Cohesion: 0.40
Nodes (5): create_db_and_tables(), main(), global_function_setup2(), fixture, session_setup1()

### Community 125 - "test_information cluster"
Cohesion: 0.53
Nodes (5): TestClient, test_get_limits_reset(), test_get_limits_reset_error(), test_get_stats_reset(), test_get_stats_reset_all_error()

### Community 126 - "test_static cluster"
Cohesion: 0.53
Nodes (5): TestClient, test_private_css(), test_private_css_nonexisting_placeholder(), test_read_web_sharepage(), test_read_web_spa()

### Community 127 - "AI Workflow Phase Docs"
Cohesion: 0.40
Nodes (3): SQLite and Alembic data model, Migration rules, Change Type evidence

### Community 128 - "test_tdd_lib cluster"
Cohesion: 0.50
Nodes (5): classify_changes(), entries: [{"status": "A"|"M"|"D"|"R087"..., "path": ...}] as from `git diff…, entry(), test_edge_classify_groups_each_kind(), test_edge_classify_ignores_deletes_and_pure_renames()

### Community 130 - "App Factory & Startup"
Cohesion: 0.60
Nodes (4): api_cmd_host(), api_cmd_service(), api_cmd_systemctl(), get

### Community 131 - "App Factory & Startup"
Cohesion: 0.40
Nodes (5): index(), get, if private.css exists return the file content, otherwise send empty response to…, Serve index.html with forced revalidation (ETag checked every time)., ui_private_css()

### Community 132 - "misc cluster"
Cohesion: 0.40
Nodes (4): GroupMediaprocessing, BaseModel, AppConfig class providing central config, Configure stages how to process images after capture.

### Community 133 - "misc cluster"
Cohesion: 0.40
Nodes (4): GroupMisc, BaseModel, AppConfig class providing central config, Quite advanced or experimental, usually not necessary to touch. Can change any…

### Community 134 - "filter_pilgram2_test cluster"
Cohesion: 0.40
Nodes (4): filter_algo(), benchmark, fixture, test_pilgram_lores_benchmark()

### Community 135 - "test_enumerate cluster"
Cohesion: 0.60
Nodes (4): TestClient, test_admin_enumerate_files(), test_admin_enumerate_serialports(), test_admin_enumerate_usbcameras()

### Community 136 - "tdd_lib cluster"
Cohesion: 0.50
Nodes (4): parse_junit_failures(), Reads pytest --junitxml. A collection failure (usually a module that does not…, test_edge_junit_collection_failure_is_file_level(), test_error_parse_junit_failures_on_empty_or_invalid_xml()

### Community 137 - "GPIO Lights Plugin"
Cohesion: 0.50
Nodes (3): contextual_serializer_password(), Any, SerializationInfo

### Community 138 - "test_debug cluster"
Cohesion: 0.67
Nodes (3): TestClient, test_read_log(), test_read_log_err()

### Community 139 - "project-memory cluster"
Cohesion: 0.67
Nodes (3): Validation Auto-Fix Prompt, BLOCKED_HUMAN state, Bootstrap Repair Loop

## Knowledge Gaps
- **83 isolated node(s):** `new-task-worktree.sh script`, `architect`, `product-manager`, `operating-model`, `Lessons Learned` (+78 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **34 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `JobModelBase` connect `Processing Event Hooks` to `App Config & Acquisition Wiring`, `multicamera cluster`, `Collage/Animation Merge`, `Actions Config Group`, `Processing API`, `video cluster`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Why does `BaseService` connect `BaseService` to `DB Models & Alembic`, `App Config & Acquisition Wiring`, `Acquisition Service`, `Processing Service`, `Media Collection Service`, `Plugin Manager`, `gpio cluster`, `Logging Service`, `Processing Event Hooks`, `processing cluster`, `Configuration Service`, `GPIO Lights Plugin`, `BaseService`, `Service Container Lifecycle`, `Information Service`, `gpio cluster`, `share cluster`, `GPIO Pin Handling`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **Why does `AcquisitionService` connect `Acquisition Service` to `DB Models & Alembic`, `App Config & Acquisition Wiring`, `Actions Config Group`, `Processing Event Hooks`, `Processing API`, `Acquisition Service`, `Acquisition Service`, `Information Service`, `Acquisition Service`, `Acquisition Service`, `Acquisition Service`, `Processing Service`, `Acquisition API Tests`, `repeatedtimer cluster`, `multicamera cluster`, `BaseService`, `video cluster`, `GPIO Lights Plugin`, `processing cluster`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `AcquisitionService` (e.g. with `BaseService` and `InformationService`) actually correct?**
  _`AcquisitionService` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `AbstractBackend` (e.g. with `StoppableThread` and `DigicamcontrolBackend`) actually correct?**
  _`AbstractBackend` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `JobModelBase` (e.g. with `JobModelAnimation` and `CaptureSet`) actually correct?**
  _`JobModelBase` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `MediacollectionService` (e.g. with `BaseService` and `Button`) actually correct?**
  _`MediacollectionService` has 8 INFERRED edges - model-reasoned connections that need verification._