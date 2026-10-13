# Graph Report - .  (2026-10-13)

## Corpus Check
- 150 files · ~141,750 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3478 nodes · 6956 edges · 222 communities (189 shown, 33 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 354 edges (avg confidence: 0.62)
- Token cost: 126,425 input · 0 output

## Community Hubs (Navigation)
- resilientservice cluster
- simple cluster
- Community 2
- Admin Files & Enumerate API
- TDD Test Repo Fixture
- Rclone Synchronizer
- Share Config Group
- Commander Plugin
- Container, Schemas & SSE
- Image/Animation Benchmarks
- Community 10
- Community 11
- DB Models & Alembic
- Community 13
- App Config & Acquisition Wiring
- DB Models & Alembic
- Plugin Manager
- misc cluster
- Background Removal (rembg)
- Filter API
- Image Processing Steps
- Abstract Camera Backend
- Backend Mode Controller
- Community 23
- Acquisition Service
- Processing Event Hooks
- Media Collection Service
- multicamera cluster
- App Factory & Startup
- Acquisition API
- Community 30
- Multicamera Steps
- AI Engineering Agents
- Community 33
- Community 34
- Community 35
- Admin Auth (JWT)
- Persona Generator
- Plugin Hookspecs & Stats
- Community 39
- Community 40
- PyAV Webcam Backend
- Gphoto2 Backend
- Picamera2 Tests
- Media Pipeline Core
- Wigglecam Backend
- Encode Benchmarks
- Acquisition Hookspec
- BaseService
- Plugin Hookspecs & Stats
- Information Service
- AI Workflow Phase Docs
- Community 52
- Community 53
- Plugin Hookspecs & Stats
- Picamera2 Backend
- Collage/Animation Merge
- Virtual Camera Source
- Community 58
- TDD Name Rules
- abstractbackend cluster
- Config Admin Tests
- Community 62
- Background Removal (rembg)
- TDD Lib & Bash Guard
- Community 65
- digiCamControl Backend
- Actions Config Group
- AI Engineering Workflows
- Community 69
- Media Pipeline Core
- Persona Prompts
- filter_pilgram2 cluster
- Community 73
- Acquisition Hookspec
- Persona Prompts
- AI Workflow Phase Docs
- Logging Service
- Community 78
- Share-on-Demand PHP
- Processing Service
- Service Container Lifecycle
- TDD Red CLI
- Picamera2 Tests
- gpio cluster
- GPIO Pin Handling
- image cluster
- AI Runtime Rules & Templates
- baseconfig cluster
- Community 89
- sse_ cluster
- repeatedtimer cluster
- encode_animation_test cluster
- Acquisition API Tests
- Image/Animation Benchmarks
- CONTRIBUTING cluster
- Community 96
- Community 97
- Community 98
- tdd_gate cluster
- scale_image_test cluster
- stream_lores_test cluster
- test_system cluster
- AI Workflow Phase Docs
- Community 104
- __init__ cluster
- Admin Auth (JWT)
- test_filter cluster
- Processing API
- Processing Event Hooks
- App Config & Acquisition Wiring
- App Config & Acquisition Wiring
- crop_image_test cluster
- Media Collection Service
- Community 114
- Community 115
- Community 116
- __init__ cluster
- Collage/Animation Merge
- share cluster
- Processing API
- printer cluster
- test_multicamera cluster
- Admin Auth (JWT)
- misc cluster
- Community 125
- Community 126
- media cluster
- resize_algorithm_test cluster
- offset_image_test cluster
- scale_video_test cluster
- test_actions cluster
- AI Engineering Workflows
- Processing API
- processing cluster
- tdd_red_guard cluster
- Abstract Camera Backend
- encode_video_test cluster
- AI Engineering Workflows
- project-memory cluster
- Community 140
- Community 141
- conftest cluster
- Picamera2 Tests
- test_share cluster
- AI Engineering Workflows
- App Factory & Startup
- Actions Config Group
- test_information cluster
- Media Collection Service
- test_static cluster
- Admin Files & Enumerate API
- test_tdd_lib cluster
- gpio cluster
- gpio cluster
- Background Removal (rembg)
- filter_pilgram2_test cluster
- test_enumerate cluster
- Community 158
- tdd_lib cluster
- GPIO Lights Plugin
- test_debug cluster
- project-memory cluster
- Community 163
- Community 164
- Community 165
- Community 166
- Persona Prompts
- Image Processing Steps
- Persona Prompts
- AI Runtime Rules & Templates
- eod-report cluster
- project-memory cluster
- Community 174
- new-task-worktree cluster
- __init__ cluster
- __init__ cluster
- __init__ cluster
- AI Engineering Workflows
- bug_report cluster
- feature_request cluster
- AI Engineering Workflows
- Persona Prompts
- Persona Prompts
- Persona Prompts
- Webcam/Virtual Backends
- pyproject cluster
- Admin Files & Enumerate API

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
- `quasar dev proxy on :9000 forwarding to backend :8000` --semantically_similar_to--> `Frontend (Node) setup: npm ci / dev proxy :8000 / build`  [INFERRED] [semantically similar]
  frontend/README.md → docs/ai/dev-environment.md
- `Worktree and branch isolation` --semantically_similar_to--> `Task worktree isolation`  [INFERRED] [semantically similar]
  docs/ai/execution.md → AGENTS.md
- `Plan: Pick-a-Booth v2 UI redesign` --references--> `/private.css user CSS override link`  [INFERRED]
  docs/plans/booth-redesign-v2.md → frontend/index.html
- `Plan: Pick-a-Booth v2 UI redesign` --conceptually_related_to--> `photobooth-frontend README`  [AMBIGUOUS]
  docs/plans/booth-redesign-v2.md → frontend/README.md
- `upstream frontend Lint workflow` --semantically_similar_to--> `frontend job: npm ci, lint:check, typecheck, vitest, build`  [INFERRED] [semantically similar]
  frontend/.github/workflows/lint.yml → .github/workflows/frontend.yml

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Event palette pipeline (theme_palette to tile/ink colours)** — docs_plans_booth_redesign_v2_theme_palette, docs_plans_booth_redesign_v2_resolvepalette, docs_plans_booth_redesign_v2_applypalette, docs_plans_booth_redesign_v2_ink, docs_plans_booth_redesign_v2_tilecolor, docs_plans_booth_redesign_v2_normalizehex [EXTRACTED 1.00]
- **Vendored frontend source to committed bundle chain** — _ai_engineering_memory_lessons_learned_frontend_git_subtree_vendoring, docs_ai_dev_environment_frontend_node_setup, _github_workflows_frontend_frontend_job, claude_no_hand_edit_bundle, agents_src_prompts_web_frontend_dev [INFERRED 0.85]
- **Strict TDD enforcement across orchestration and CI** — docs_ai_testing_strategy_strict_tdd, docs_ai_testing_strategy_test_case_order, docs_ai_testing_strategy_tdd_gate, agents_src_prompts_project_manager_contract_first_dispatch, docs_ai_agent_orchestration_dispatch_round_structure [EXTRACTED 1.00]
- **Canonical flow mandatory doc loads** — agents_canonical_task_flow, docs_ai_plan_template, docs_ai_execution, docs_ai_testing_strategy, docs_ai_autonomous_engineering [EXTRACTED 0.90]
- **Agent role contracts** — ai_engineering_agents_product_manager, ai_engineering_agents_architect, ai_engineering_agents_coordinator, ai_engineering_agents_implementer, ai_engineering_agents_reviewer, ai_engineering_agents_qa, ai_engineering_agents_reporter [EXTRACTED 1.00]
- **Task lifecycle state docs** — ai_engineering_core_task_lifecycle, ai_engineering_core_task_state_machine, ai_engineering_core_task_state_machine_skipped_already_implemented, ai_engineering_core_task_state_machine_blocked_states, ai_engineering_core_task_state_machine_waiting_approval [INFERRED 0.85]
- **Report templates** — ai_engineering_templates_execution_report_doc, ai_engineering_templates_review_report_doc, ai_engineering_templates_qa_report_doc, ai_engineering_templates_pr_report_doc, ai_engineering_templates_eod_report_doc [INFERRED 0.75]
- **Phase-loaded AI workflow workflow docs** — _ai_engineering_workflows_task_intake, _ai_engineering_workflows_feature_development, _ai_engineering_workflows_review_process, _ai_engineering_workflows_release_process, _ai_engineering_workflows_bug_fix, _ai_engineering_workflows_blocker_handling, _ai_engineering_workflows_daily_cycle [INFERRED 0.85]
- **GitHub Actions CI workflows** — _github_workflows_ai_gates, _github_workflows_benchmarks, _github_workflows_cicd, _github_workflows_linter, _github_workflows_pytests [INFERRED 0.85]

## Communities (222 total, 33 thin omitted)

### Community 0 - "resilientservice cluster"
Cohesion: 0.05
Nodes (32): Common, BaseModel, WledConfig, Enum, Event, hookimpl, State, To start the resilient service (+24 more)

### Community 1 - "simple cluster"
Cohesion: 0.05
Nodes (42): PathLike, api_delete_calibration_delete(), delete, CalibrationDataExtrinsics, CalibrationDataIntrinsics, CalibrationBase, PersistableDataclass, Path (+34 more)

### Community 2 - "Community 2"
Cohesion: 0.04
Nodes (53): CharucoBoardDefinition, charucoBoardDefinitionModel, imageUrl, loading, postBoardDefinition(), props, getConfigurables(), AlignType (+45 more)

### Community 3 - "Admin Files & Enumerate API"
Cohesion: 0.06
Nodes (54): Body, api_get_rclone_remotes(), api_get_serial_ports(), api_get_usbcameras(), get_search(), get, api_clearrecycledir(), create_upload_file() (+46 more)

### Community 4 - "TDD Test Repo Fixture"
Cohesion: 0.10
Nodes (50): git(), make_repo(), Path, Repo, run_script(), write(), cited_paths(), Path (+42 more)

### Community 5 - "Rclone Synchronizer"
Cohesion: 0.05
Nodes (23): Mediaitem, RcloneApi, UUID, https://photobooth-app.org/setup/configuration/qrshareservice/, setup the resource right before run_service logic, tear down the resource right after run_service logic and in case of crashes, service logic to be run when the service is started, ShareOnDemandService (+15 more)

### Community 6 - "Share Config Group"
Cohesion: 0.07
Nodes (46): Container, stop all services first (reverse order), then start them again., GroupShare, BaseModel, AppConfig class providing central config, Configure share or print actions., Configure additional parameter for the share command to input by the user., Configure options to share or print images. (+38 more)

### Community 7 - "Commander Plugin"
Cohesion: 0.11
Nodes (31): eventHooks, field_validator, Commander, Event, hookimpl, MediaitemTypes, State, ThreadCommand (+23 more)

### Community 8 - "Container, Schemas & SSE"
Cohesion: 0.07
Nodes (26): MediaitemPublic, BaseModel, ShareLimitsPublic, UsageStatsPublic, Handle all media collection related functions, BaseModel, # FIXME: workaround for testing until testing with mocks/patching works well..., basic class for sse events (+18 more)

### Community 9 - "Image/Animation Benchmarks"
Cohesion: 0.07
Nodes (34): BytesIO, benchmark, test_transpose_piexif(), test_transpose_pillow(), transpose_piexif(), transpose_pillow(), ffmpeg_hq_optimizedquality_scale(), ffmpeg_hq_optimizedspeed_scale() (+26 more)

### Community 10 - "Community 10"
Cohesion: 0.06
Nodes (35): Props, subtitle, { t }, title, againColor, confirmDeleteDialog, emit, ghostCount (+27 more)

### Community 11 - "Community 11"
Cohesion: 0.07
Nodes (35): props, { stalled, markFrameReceived }, {
  status: webSocketStreamStatus,
  open: openWebSocketStream,
  close: closeWebSocketStream,
  ws: wsRef,
}, streamRenderer, visibility, websocketStreamUrl, CanvasPair, computeTransparentBoundingBox() (+27 more)

### Community 12 - "DB Models & Alembic"
Cohesion: 0.06
Nodes (24): datetime, AppConfig class providing central config, GpioLight, BaseModel, AppConfig class providing central config file called appconfig_ to avoid…, AppConfig class providing central config file called appconfig_ to avoid…, AppConfig class providing central config, GroupMediaprocessing (+16 more)

### Community 13 - "Community 13"
Cohesion: 0.06
Nodes (32): configurationStore, connected, initialInitDone, mediacollectionStore, $q, showConnectionOverlay, stateStore, store (+24 more)

### Community 14 - "App Config & Acquisition Wiring"
Cohesion: 0.14
Nodes (20): manage up to two photobooth-app backends in this module, AnimationConfigurationSet, BaseConfigurationSet, CollageConfigurationSet, MulticameraConfigurationSet, MulticameraJobControl, MultiImageJobControl, Configure job control affecting the procedure. (+12 more)

### Community 15 - "DB Models & Alembic"
Cohesion: 0.08
Nodes (16): DeclarativeBase, listens_for, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Base, Cacheditem (+8 more)

### Community 16 - "Plugin Manager"
Cohesion: 0.09
Nodes (14): BasePlugin, ConfigurationService, Any, AnyStr, PluginManagerService, When the pluginmanager is started, it will start all registered plugins that…, When the pluginmanager is stoppped, it will stop all registered plugins that…, configuration_service() (+6 more)

### Community 17 - "misc cluster"
Cohesion: 0.07
Nodes (29): Color, field_serializer, LogCaptureFixture, GroupActions, Configure actions like capture photo, video, collage and animations., GroupCommon, BaseModel, SerializationInfo (+21 more)

### Community 18 - "Background Removal (rembg)"
Cohesion: 0.11
Nodes (25): SessionOptions, naive_cutout(), Any, PILImage, The util is very much inspired by https://github.com/danielgatis/rembg Thank…, Remove the background from an input image., remove(), new_session() (+17 more)

### Community 19 - "Filter API"
Cohesion: 0.12
Nodes (31): api_get_calibration_generate_charucoboard(), api_get_calibration_stats(), api_get_result(), api_post_calibrate_all(), CalibrationRequest, CharucoBoardDefinition, BaseModel, get (+23 more)

### Community 20 - "Image Processing Steps"
Cohesion: 0.16
Nodes (36): TextsConfig, ImageContext, process_image_inner(), Unified handling of images that are just one single capture: 1pictaken…, FillBackgroundStep, ImageFrameStep, ImageMountStep, optimized function for use on single images. resulting size is derived from the… (+28 more)

### Community 21 - "Abstract Camera Backend"
Cohesion: 0.12
Nodes (20): AbstractBackend, BackendStats, MulticamRequest, ABC, # TODO: validate 0.5 tolerance., defines some common stats - if backend supports, they return these properties,…, StillRequest, Picamera2Stats (+12 more)

### Community 22 - "Backend Mode Controller"
Cohesion: 0.08
Nodes (16): Modes, ModeController, Path, Einfacher Mode-Controller mit: - requested_mode (Thread-agnostisch) -…, usually requested when creating a video but also for livestream. livestream…, Monitor thread function to request standby if no livestream is requested for…, Wird im stream-thread aufgerufen, wenn es passend für einen potentiellen mode-…, called during device setup (+8 more)

### Community 23 - "Community 23"
Cohesion: 0.06
Nodes (25): applyFilterClick(), emit, props, available_filter, configurationStore, currentMediaitem, currentMediaitemNumber, displayIndeterminateProgressbar (+17 more)

### Community 24 - "Acquisition Service"
Cohesion: 0.08
Nodes (18): AcquisitionService, Path, called by job processor when a countdown for video is started, Gather stats from active backends. Backend stats are converted to dict to be…, called by job processor when a countdown for stills is started, _acqs(), fixture, get video from service (+10 more)

### Community 25 - "Processing Event Hooks"
Cohesion: 0.07
Nodes (12): JobModelBase, ABC, Event, T, UUID, eval user / automated input got from transition, when ALL captures are completed for the job, the very last step, used to notify the ui the statemachin is going done now (+4 more)

### Community 26 - "Media Collection Service"
Cohesion: 0.11
Nodes (21): MediacollectionService, UUID, Handle all image related stuff, client(), client_authenticated(), global_function_setup1(), global_function_setup2(), fixture (+13 more)

### Community 27 - "multicamera cluster"
Cohesion: 0.07
Nodes (6): overlay used during a job, UiFrameOverlay, JobModelMulticamera, Event, JobModelVideo, Event

### Community 28 - "App Factory & Startup"
Cohesion: 0.10
Nodes (21): FastAPI, _create_app(), lifespan(), api_get_config_current_active(), get, get_log_latest(), get, provide latest logfile to download (+13 more)

### Community 29 - "Acquisition API"
Cohesion: 0.10
Nodes (26): asyncio, api_cmd_aquisition_capturemode_get(), api_multicam_get(), api_multicam_loadfile_get(), api_still_get(), get, Path, set backends to preview or capture mode (usually automatically switched as… (+18 more)

### Community 30 - "Community 30"
Cohesion: 0.13
Nodes (13): setup(), setup(), setup(), setup(), setup(), setup(), setup(), hasListApi() (+5 more)

### Community 31 - "Multicamera Steps"
Cohesion: 0.12
Nodes (18): MatLike, MulticameraContext, AlignAsPerCalibrationStep, AutoPivotPointStep, CropCommonAreaStep, OffsetPerOpticalFlowStep, Image, NextStep (+10 more)

### Community 32 - "AI Engineering Agents"
Cohesion: 0.10
Nodes (28): architect, coordinator, implementer, product-manager, qa, reporter, reviewer, PILOT_FROZEN activation (+20 more)

### Community 33 - "Community 33"
Cohesion: 0.07
Nodes (29): autoprefixer, devDependencies, autoprefixer, globals, @intlify/unplugin-vue-i18n, openapi-typescript, oxfmt, oxlint (+21 more)

### Community 34 - "Community 34"
Cohesion: 0.07
Nodes (29): @fontsource/manrope, @fontsource/sora, dependencies, @fontsource/manrope, @fontsource/sora, @jsonforms/core, @jsonforms/vue, lucide-vue-next (+21 more)

### Community 35 - "Community 35"
Cohesion: 0.08
Nodes (22): activeSlot, emit, hostSlot, { icon = 'sym_o_arrow_back_ios_new' }, ReturnButtonSlot, ReturnButtonSlotOptions, slotOptions, { t } (+14 more)

### Community 36 - "Admin Auth (JWT)"
Cohesion: 0.14
Nodes (25): oauth2_scheme, OAuth2PasswordRequestForm, login_for_access_token(), Depends, get, post, read_users_me(), api_get_statscounter_reset_all() (+17 more)

### Community 37 - "Persona Generator"
Cohesion: 0.13
Nodes (24): Persona, check(), claude_file(), compute_targets(), _escape(), find_duplicate_owned_globs(), generate(), load_personas() (+16 more)

### Community 38 - "Plugin Hookspecs & Stats"
Cohesion: 0.11
Nodes (16): Protocol, Common, OndemandShareConfig, BaseModel, RcloneConfig, RemoteConfig, ShareConfig, RcloneApi (+8 more)

### Community 39 - "Community 39"
Cohesion: 0.08
Nodes (21): getLanguageName(), i18n, preferredLanguages, builddate, confirm_clear_recycle_directory, confirm_delete_all, confirm_install_systemctl, confirm_reboot_host (+13 more)

### Community 40 - "Community 40"
Cohesion: 0.08
Nodes (18): { size = 24, strokeWidth = 2.2 }, store, adminButtonInvisible, btnAdminClickCounter, configurationStore, fixedSize, frameOverlay, frontpageText (+10 more)

### Community 41 - "PyAV Webcam Backend"
Cohesion: 0.10
Nodes (12): InputContainer, Packet, WebcamPyavBackend, webcameras(), PermanentFault, Raised from within the services when the service should not attempt recovery., backend_pyav(), fixture (+4 more)

### Community 42 - "Gphoto2 Backend"
Cohesion: 0.12
Nodes (10): GpEvents, Gphoto2Backend, GpWidgets, Enum, Gphoto2Parameters, Configure different settings when switching between modes., backend_gphoto2(), fixture (+2 more)

### Community 43 - "Picamera2 Tests"
Cohesion: 0.12
Nodes (23): is_rpi(), detect if computer is a raspberry pi (any model) Returns: bool: true is…, backend_picamera2(), fixture, get lores and hires images from backend and assert, run_around_tests(), test_get_video_picamera2(), test_getImages() (+15 more)

### Community 44 - "Media Pipeline Core"
Cohesion: 0.12
Nodes (14): Context, ErrorHandler, _default_error_handler(), Pipeline, PipelineCursor, PipelineError, PipelineStep, Any (+6 more)

### Community 45 - "Wigglecam Backend"
Cohesion: 0.13
Nodes (11): Path, Trigger a capture request and collect hi-res images from all cameras., Background loop to receive lores frames., WigglecamBackend, GroupCameraWigglecam, WigglecamNodes, backend_wigglecam(), fixture (+3 more)

### Community 46 - "Encode Benchmarks"
Cohesion: 0.13
Nodes (22): cv2_encode_jpg(), cv2_encode_png_lossless(), cv2_encode_webp(), image(), image_hires(), image_lores(), library(), library_yuv420() (+14 more)

### Community 47 - "Acquisition Hookspec"
Cohesion: 0.12
Nodes (13): hookspec, PluginAcquisitionSpec, PluginManagementSpec, init is run on app initialization. plugins are reinitialized on container…, plugin start is called in last step during container.start, plugin stop is called in first step during container.stop, the information service requests reqular statistics from the plugin to display…, triggers before a shot (+5 more)

### Community 48 - "BaseService"
Cohesion: 0.12
Nodes (8): skipif, BaseService, EnumStatus, Enum, Base service and resources module., All services (factory/singleton) and resources derive from this base class…, SystemService, test_systemd_control()

### Community 49 - "Plugin Hookspecs & Stats"
Cohesion: 0.14
Nodes (14): SynchronizerConfig, hookimpl, Path, UUID, Synchronizer, fixture, Create a SynchronizerRclone with mocked config + mocked rclone client., sync() (+6 more)

### Community 50 - "Information Service"
Cohesion: 0.13
Nodes (3): InformationService, Any, Raspberry Pi system health monitor using vcgencmd. Decode throttled bitmask…

### Community 51 - "AI Workflow Phase Docs"
Cohesion: 0.12
Nodes (15): SQLite and Alembic data model, Completion Gate, Integration sequence, Plan template skeleton, Test Matrix, Graphify discovery first, Migration rules, Mandatory Pull Request Evidence (+7 more)

### Community 52 - "Community 52"
Cohesion: 0.10
Nodes (18): ArrayListRendererEntry, arrayRenderers, BooleanToggleControlRendererEntry, ColorControlRendererEntry, controlRenderers, EnumArrayControlRendererEntry, EnumControlRendererEntry, isRangeControl (+10 more)

### Community 53 - "Community 53"
Cohesion: 0.09
Nodes (22): CELLS, DELAYS, { label }, ajv, autoReloadServicesOnSave, configNav, configurables, configuration (+14 more)

### Community 54 - "Plugin Hookspecs & Stats"
Cohesion: 0.19
Nodes (12): PipelineStats, PrioritizedJob, ThreadedImmediateSyncPipeline, CopyOperation, DeleteOperation, JobResult, JobStatus, Enum (+4 more)

### Community 55 - "Picamera2 Backend"
Cohesion: 0.11
Nodes (6): Picamera2Backend, Path, Every camera tuning file usually has at least "normal", "short" and "long"…, function that returns None if value is None, otherwise round is applied and…, picamera2 has local start_recording, which overrides the abstract class…, on start set autofocus to continuous if requested by config or auto and trigger…

### Community 56 - "Collage/Animation Merge"
Cohesion: 0.20
Nodes (14): PluginFilters, AnimationMergeDefinition, CollageMergeDefinition, BaseModel, AnimationContext, AddPredefinedImagesStep, PostPredefinedImagesStep, NextStep (+6 more)

### Community 57 - "Virtual Camera Source"
Cohesion: 0.13
Nodes (4): Path, for other threads to receive a hq JPEG image, VirtualCameraBackend, test_optimize_mode()

### Community 58 - "Community 58"
Cohesion: 0.11
Nodes (15): emit, formData, onSubmit(), props, {
  height = 96,
  bg = 'var(--pb-surface-2)',
  fg = 'var(--pb-text)',
  bordered = false,
  icon,
  iconSize = 28,
  fontSize = 24,
  pill = false,
  padding,
  block = false,
  disabled = false,
}, rootStyle, lucide, {
  name,
  size = 24,
  strokeWidth = 2,
} (+7 more)

### Community 59 - "TDD Name Rules"
Cohesion: 0.15
Nodes (22): check_names(), extract_test_names(), judge_red(), parse_waivers(), added: names introduced by the diff (any file). new_files: full ordered names…, Test functions pytest would collect, in declaration order. Strings, comments…, added(), test_edge_extract_handles_async_methods_and_skips_fixtures() (+14 more)

### Community 60 - "abstractbackend cluster"
Cohesion: 0.10
Nodes (11): Framerate, LoresBroadcastRes, Orientation, public api, non-blocking, call by backends implementation when frame is delivered, so the fps can be…, To start the backend to serve, Thread-safe rolling-window FPS calculator., Return remaining nanoseconds until the next frame should be processed. Positive… (+3 more)

### Community 61 - "Config Admin Tests"
Cohesion: 0.14
Nodes (19): AppConfig, AppConfig class glueing all together In the case where a value is specified for…, patch, TestClient, test_config_endpoints_ui(), test_config_getschema(), test_config_patch(), test_config_post_validationerror() (+11 more)

### Community 62 - "Community 62"
Cohesion: 0.10
Nodes (10): setup(), setup(), CombinatorProps, AllOfRendererEntry, AnyOfOptionalRendererEntry, AnyOfRendererEntry, complexRenderers, EnumArrayRendererEntry (+2 more)

### Community 63 - "Background Removal (rembg)"
Cohesion: 0.12
Nodes (9): ModnetSession, PILImage, Predicts the output masks for the input image using the inner session.…, PILImage, Predicts the output masks for the input image using the inner session.…, U2netSession, PILImage, Predicts the mask for the given image using the U2netp model. Parameters: img… (+1 more)

### Community 64 - "TDD Lib & Bash Guard"
Cohesion: 0.13
Nodes (20): expr, find_bash_write_targets(), _is_fixture(), is_guarded_source(), _is_path_arg(), kind_of(), NamedTuple, Shared rules for the TDD gate (CI), `uv run poe tdd:red` (local) and the Claude… (+12 more)

### Community 65 - "Community 65"
Cohesion: 0.12
Nodes (9): setup(), setup(), setup(), useAjv(), useQuasarLayout(), categoryTitle(), CONFIG_NAV_KEY, ConfigNavState (+1 more)

### Community 66 - "digiCamControl Backend"
Cohesion: 0.13
Nodes (8): HTTPServer, DigicamcontrolBackend, r""" Digicamcontrol backend implementation Quirks: - using webfrontend only…, GroupCameraDigicamcontrol, backend_digicamcontrol_emulated(), fixture, test_emulated_get_images_disable_liveview_recovery_more_retries(), test_optimize_mode()

### Community 67 - "Actions Config Group"
Cohesion: 0.18
Nodes (9): SingleImageConfigurationSet, SingleImageJobControl, SingleImageProcessing, JobModelImage, Event, test_jobmodel_start_count(), test_jobmodel_start_count_bigger_offset(), test_jobmodel_start_count_equal() (+1 more)

### Community 68 - "AI Engineering Workflows"
Cohesion: 0.11
Nodes (17): ADR-0001 AI workflow port, ADR-0002 Claude Code only runtime, Blocker Handling workflow, Task Intake workflow, Caveman ultra policy, Core principles, Strict TDD (principle 6b), Structured autonomous work orders (+9 more)

### Community 69 - "Community 69"
Cohesion: 0.11
Nodes (15): isButton, largeGlass, PillSize, preset, PRESETS, resolvedFontSize, resolvedIconSize, rootStyle (+7 more)

### Community 70 - "Media Pipeline Core"
Cohesion: 0.22
Nodes (12): VideoContext, BoomerangStep, LoopStep, NextStep, benchmark, test_encode_boomerang_pyav(), test_loop_pyav(), video_boomerangPyav_stage() (+4 more)

### Community 71 - "Persona Prompts"
Cohesion: 0.15
Nodes (18): Automatic agent routing default, project-manager persona prompt, Contract-First Dispatch, Feature spec format (testable acceptance criteria), web-frontend-dev persona prompt, Alembic migrations run unattended at every app start, Agent Orchestration, Dispatch Round Structure (Rounds 0-4, QA fan-out) (+10 more)

### Community 72 - "filter_pilgram2 cluster"
Cohesion: 0.18
Nodes (8): available_filter, BaseFilter, FilterPilgram2Config, FilterPilgram2, hookimpl, Image, filter_pilgram2_plugin(), fixture

### Community 73 - "Community 73"
Cohesion: 0.15
Nodes (10): setup(), setup(), createEmptyStyles(), useStyles(), NestedInfo, useComputedLabel(), useControlAppliedOptions(), useQuasarBasicControl() (+2 more)

### Community 74 - "Acquisition Hookspec"
Cohesion: 0.15
Nodes (12): DisplayEnum, GenericStats, StrEnum, SubList, SubStats, PluginMediaprocessingSpec, Enum, Image (+4 more)

### Community 75 - "Persona Prompts"
Cohesion: 0.13
Nodes (18): fastapi-backend-dev persona prompt, CLAUDE.md project context, Config source order: init > config.json > dotenv > env > secrets, Never commit to main; always a PR (gh pr create --repo OwlRepo/pick-a-booth), Persona definitions generated via uv run poe agents:generate, photobooth-app (upstream), pick-a-booth (OwlRepo fork of photobooth-app), GLOBAL_POLICY block appended to every persona (+10 more)

### Community 76 - "AI Workflow Phase Docs"
Cohesion: 0.16
Nodes (16): Development Environment, No shared DEV server; everything runs locally per worktree, Repository Map, Plan: Pick-a-Booth v2 UI redesign, applyPalette(), R8: no boomerang media_type, boomerang shows Video badge, Design tokens (tokens.scss, Sora/Manrope), Deterministic-spec waiver for 22 screens (+8 more)

### Community 77 - "Logging Service"
Cohesion: 0.13
Nodes (7): ExceptHookArgs, LogRecord, ConsoleColorFormatter, EventstreamLogHandler, LoggingService, mute some logger by rasing their log level, Logging handler to emit events to eventstream; to be displayed in console.log…

### Community 78 - "Community 78"
Cohesion: 0.14
Nodes (12): { fit = 'contain' }, badge, props, { t }, carouselRef, carouselTransition(), currentMediaitemId, emit (+4 more)

### Community 79 - "Share-on-Demand PHP"
Cohesion: 0.22
Nodes (3): RuntimeException, AuthException, ShareService

### Community 80 - "Processing Service"
Cohesion: 0.16
Nodes (4): ProcessingService, ActionType, if queue is initialized on _external_cmd_queue, a user request is waited for., userEvents

### Community 81 - "Service Container Lifecycle"
Cohesion: 0.23
Nodes (8): DigitalOutputDevice, Events, GpioLightsConfig, AppDigitalOutputDevice, GpioLights, Event, hookimpl, State

### Community 82 - "TDD Red CLI"
Cohesion: 0.22
Nodes (15): changed_entries(), git(), main(), parse_args(), Exception, Path, `uv run poe tdd:red`: run this branch's changed tests BEFORE implementing and…, Committed + staged + unstaged changes against the merge-base, plus untracked… (+7 more)

### Community 83 - "Picamera2 Tests"
Cohesion: 0.15
Nodes (3): Convert JPG/MJPG and YUVY pixelformat to output JPG, WebcamV4lBackend, test_optimize_mode()

### Community 84 - "gpio cluster"
Cohesion: 0.14
Nodes (7): GroupHardwareInputOutput, BaseModel, Configure hardware GPIO, keyboard and more. Find integration information in the…, GpioService, ActionType, gpio_service(), fixture

### Community 85 - "GPIO Pin Handling"
Cohesion: 0.22
Nodes (12): PinHandler, pinhandler1(), patch, test_action_buttons(), test_button_reboot(), test_button_share(), test_button_shutdown(), test_pinhandler_register_longpress() (+4 more)

### Community 86 - "image cluster"
Cohesion: 0.18
Nodes (7): RembgModelType, draw_rotated_text(), Image, NextStep, Draw text at an angle into an image, takes the same arguments as Image.text()…, RemovebgStep, PipelineError

### Community 87 - "AI Runtime Rules & Templates"
Cohesion: 0.14
Nodes (15): ADR Template, Execution Report Template, docs/ai/plan-template.md, Plan Template (short form), QA Report Template, Review Report Template, uv run poe agents:lint, Agent Contract Validation (+7 more)

### Community 88 - "baseconfig cluster"
Cohesion: 0.16
Nodes (6): BaseSettings, PydanticBaseSettingsSource, BaseConfig, Remove allof that would interfere with the normal processing of jsonforms…, Get schema to build UI. Schema is polished to the needs of UI, Persist config to file

### Community 89 - "Community 89"
Cohesion: 0.24
Nodes (12): colors, emit, props, triggerButtonClick(), visibleTriggers, applyPalette(), DEFAULT_PALETTE, ink() (+4 more)

### Community 90 - "sse_ cluster"
Cohesion: 0.16
Nodes (8): Request, get, Eventstream to feed clients with server generated events and data, subscribe(), class providing central sse, Client, Class each individual client connected, SseService

### Community 91 - "repeatedtimer cluster"
Cohesion: 0.16
Nodes (6): Repeat Timer in separate thread for tasks to be executed in intervals, Call a function after a specified number of seconds: t = Timer(30.0, f,…, Stop the timer if it hasn't finished yet., RepeatedTimer, Timer, Thread

### Community 92 - "encode_animation_test cluster"
Cohesion: 0.21
Nodes (14): dummy_images(), library(), pillow_encode_avif(), pillow_encode_gif(), pillow_encode_webp(), Any, benchmark, fixture (+6 more)

### Community 93 - "Acquisition API Tests"
Cohesion: 0.28
Nodes (14): capture(), patch, TestClient, test_aquire_multiple_nomodechange(), test_aquire_multiple_withmodechange(), test_aquire_still_capturemode(), test_aquire_still_exception(), test_capture_multicamera() (+6 more)

### Community 94 - "Image/Animation Benchmarks"
Cohesion: 0.28
Nodes (14): _container(), fixture, this function processes single images (in contrast to collages or videos), test_animation(), test_capture(), test_capture_zero_countdown(), test_collage_auto_approval(), test_collage_manual_abort() (+6 more)

### Community 95 - "CONTRIBUTING cluster"
Cohesion: 0.14
Nodes (13): accessibility-auditor persona prompt, WCAG 2.1 AA kiosk/admin checklist, ui-ux-designer persona prompt, Kiosk constraints (44x44 targets, no hover-only, reduced motion), Mandatory loading/empty/success/error states, Don't hand-edit hashed src/web/frontend/assets; rebuild from frontend/, Commercialization code contribution policy, Crowdin translation workflow (+5 more)

### Community 96 - "Community 96"
Cohesion: 0.14
Nodes (13): allowScripts, esbuild@0.25.12, @parcel/watcher@2.6.0, author, description, name, typescript, overrides (+5 more)

### Community 97 - "Community 97"
Cohesion: 0.21
Nodes (3): defaultStyles, Styles, mergeStyles()

### Community 98 - "Community 98"
Cohesion: 0.18
Nodes (12): isPortrait, showImage, userAbort(), userConfirm(), userReject(), actionResetLimitsConfirmed(), actionResetStatsConfirmed(), doShareAction() (+4 more)

### Community 99 - "tdd_gate cluster"
Cohesion: 0.31
Nodes (13): changed_entries(), collect_names(), GateError, git(), main(), Exception, CI TDD gate for pull requests. Rules: docs/ai/testing-strategy.md "Strict TDD".…, Runs the PR's test files against the merge-base source in a throwaway worktree. (+5 more)

### Community 100 - "scale_image_test cluster"
Cohesion: 0.24
Nodes (13): cv2_scale(), image(), image_hires(), image_lores(), library(), pillow_scale(), benchmark, fixture (+5 more)

### Community 101 - "stream_lores_test cluster"
Cohesion: 0.26
Nodes (13): benchmark, pyav_cv2_scale(), pyav_pillow_scale(), pyav_scale_cv2_encode(), pyav_scale_simplejpeg_encode(), pyav_simplejpeg_scale(), pyav_turbojpeg_scale(), test_pyav_cv2_scale() (+5 more)

### Community 102 - "test_system cluster"
Cohesion: 0.24
Nodes (13): fixture, patch, TestClient, system_host_endpoint(), system_nonexistant_endpoint(), system_service_endpoint(), system_systemctl_endpoint(), system_systemctl_installuninstall_endpoint() (+5 more)

### Community 103 - "AI Workflow Phase Docs"
Cohesion: 0.19
Nodes (12): Canonical Task Flow, Graphify discovery, Task worktree isolation, Origin freshness and app-managed worktrees, Implementation rules, Mandatory Graphify closeout, QA mode, Review mode (+4 more)

### Community 104 - "Community 104"
Cohesion: 0.15
Nodes (9): Props, remainingSeconds, ringProgress, showBox, showCountdown, showMessage, startDuration, stepsActive (+1 more)

### Community 105 - "__init__ cluster"
Cohesion: 0.32
Nodes (8): PluginStatemachineSpec, Event, MediaitemTypes, State, job processor before a transition takes place. for details see python…, job processor when exit a state. for details see python statemachine library, job processor when the new state is entered. for details see python…, job processor after a transition took place. for details see python…

### Community 106 - "Admin Auth (JWT)"
Cohesion: 0.19
Nodes (12): api_get_config_current_active(), api_get_config_schema(), api_get_configurables(), api_post_config_current(), api_reset_all_config(), api_reset_config(), Any, AnyStr (+4 more)

### Community 107 - "test_filter cluster"
Cohesion: 0.26
Nodes (11): Example 2nd-level subpackage., TestClient, test_apply_filter(), test_apply_filter_nonexistentfilter(), test_get_avail_filter(), test_get_avail_filter_err(), test_preview_filter_1977(), test_preview_filter_nonexistentfilter() (+3 more)

### Community 108 - "Processing API"
Cohesion: 0.33
Nodes (11): deprecated, Path, scale a jpeg buffer to another buffer using pillow, Scale an animated image sequence (GIF/WebP/AVIF) and preserve frame durations., resize(), resize_gif_pyav(), resize_jpeg(), resize_jpeg_pillow() (+3 more)

### Community 109 - "Processing Event Hooks"
Cohesion: 0.29
Nodes (4): DbListenter, PluginEventHooks, Event, State

### Community 112 - "crop_image_test cluster"
Cohesion: 0.24
Nodes (8): image(), image_hires(), image_lores(), library(), benchmark, fixture, test_libraries_encode_hires(), test_libraries_encode_lores()

### Community 113 - "Media Collection Service"
Cohesion: 0.32
Nodes (11): fixture_reset(), modules_client(), fixture, patch, TestClient, test_id_filenotfound_exception(), test_latest_filenotfound_exception(), test_print_check_blocking() (+3 more)

### Community 114 - "Community 114"
Cohesion: 0.22
Nodes (11): Lessons Learned (append-only), Frontend source vendored via git subtree, No bundle-freshness CI diff, frontend CI workflow (frontend.yml), frontend job: npm ci, lint:check, typecheck, vitest, build, Upstream sync: keep additive changes in new files, Amendment: frontend CI in new frontend.yml (not ci.yml), R6: upstream frontend has no license file (+3 more)

### Community 115 - "Community 115"
Cohesion: 0.18
Nodes (11): scripts, build, check-types, dev, format, generate-types, lint, lint:check (+3 more)

### Community 116 - "Community 116"
Cohesion: 0.20
Nodes (8): emit, props, remainingSeconds, returnCaption, startTimer(), { t }, percent, {
  progress,
  color = 'var(--t3)',
  left,
  right,
  ariaLabel,
}

### Community 117 - "__init__ cluster"
Cohesion: 0.24
Nodes (7): PluginMediacollectionSpec, Path, UUID, files added to collection. priority modifier allows sync queues to upload…, # list of files that were updated (example, filter applied), deleted a file from collection, share backends shall create a link to the mediaitem ressource so it can be used…

### Community 118 - "Collage/Animation Merge"
Cohesion: 0.33
Nodes (7): CollageContext, MergeCollageStep, Image, NextStep, Testing Mediaprocessing collage, test_collage_stage(), test_collage_stage_definition_not_matching_with_no_captured()

### Community 120 - "Processing API"
Cohesion: 0.22
Nodes (5): CountdownTimer, test that 0 countdown doesn't block whole application, check that timer is accurate enough, test_countdowntimer_accuracy(), test_countdowntimer_zero()

### Community 121 - "printer cluster"
Cohesion: 0.33
Nodes (10): classify_linux(), classify_windows(), get_printer_status(), get_printer_status_linux(), get_printer_status_windows(), monitor_printer(), on_state_change(), PrinterStateChange (+2 more)

### Community 122 - "test_multicamera cluster"
Cohesion: 0.38
Nodes (10): patch, Path, TestClient, test_delete_calibration_success(), test_generate_charucoboard_failure(), test_generate_charucoboard_success(), test_get_result_failure(), test_get_result_success() (+2 more)

### Community 123 - "Admin Auth (JWT)"
Cohesion: 0.31
Nodes (10): client_authenticated(), fixture, TestClient, test_login(), test_login_user_ok_password_wrong(), test_login_wrong_user(), test_user(), test_user_me() (+2 more)

### Community 124 - "misc cluster"
Cohesion: 0.29
Nodes (9): le, Query, api_gallery_delete(), api_gallery_delete_all(), api_getitem(), api_getitems(), delete, get (+1 more)

### Community 125 - "Community 125"
Cohesion: 0.25
Nodes (5): actionButtonClick(), emit, StatEntry, SubList, SubStats

### Community 127 - "media cluster"
Cohesion: 0.42
Nodes (8): head, api_getitems_get(), api_getitems_head(), DimensionTypes, get, UUID, head used for download portal to check if the file is available without…, _serve_media_item()

### Community 128 - "resize_algorithm_test cluster"
Cohesion: 0.33
Nodes (8): parametrize, Resampling, cv2_resize(), pil_resize(), benchmark, Image, test_cv2_resize(), test_pil_resize()

### Community 129 - "offset_image_test cluster"
Cohesion: 0.31
Nodes (8): image_hires_rgb(), benchmark, fixture, Image, recenter_image(), recenter_image_chops(), test_recenter_image(), test_recenter_image_chops()

### Community 130 - "scale_video_test cluster"
Cohesion: 0.33
Nodes (8): ffmpeg_h264_scale(), benchmark, fixture, pyav_h264_scale(), test_ffmpeg_h264_scale(), test_pyav_scale(), thread_type(), threading_number()

### Community 131 - "test_actions cluster"
Cohesion: 0.39
Nodes (8): TestClient, test_chose_1pic(), test_chose_1pic_occupied(), test_chose_1pic_otherexception(), test_chose_animation(), test_chose_collage(), test_chose_multicamera(), test_chose_video()

### Community 132 - "AI Engineering Workflows"
Cohesion: 0.32
Nodes (6): Autonomous Engineering Layer (.ai-engineering), autonomous-engineering.yaml config, doc link test (test_doc_links.py), Activation states PILOT_FROZEN/ACTIVE/RELEASE_FROZEN, Bootstrap validation workflow, Pilot mode (PILOT_FROZEN)

### Community 133 - "Processing API"
Cohesion: 0.39
Nodes (7): BackgroundTasks, api_cmd_abort_get(), api_cmd_confirm_get(), api_cmd_reject_get(), api_get_preview_image_filtered(), get, UUID

### Community 134 - "processing cluster"
Cohesion: 0.32
Nodes (3): JobModelType, FrontendNotifierEventHooks, SseEventProcessStateinfo

### Community 135 - "tdd_red_guard cluster"
Cohesion: 0.46
Nodes (7): git(), main(), marker_problem(), Path, Claude Code PreToolUse hook: blocks writes to src/photobooth logic until `uv…, The target may not exist yet (Write of a new file); resolve through the nearest…, resolve_target()

### Community 136 - "Abstract Camera Backend"
Cohesion: 0.25
Nodes (4): Path, A standalone video recorder that: - runs in its own thread - pulls lores frames…, Start recording. Returns the output filepath., SoftwareVideoRecorder

### Community 137 - "encode_video_test cluster"
Cohesion: 0.36
Nodes (7): process_ffmpeg(), process_pyav(), benchmark, fixture, run_around_tests(), test_process_ffmpeg(), test_process_pyav()

### Community 138 - "AI Engineering Workflows"
Cohesion: 0.33
Nodes (7): Daily Cycle workflow, Feature Development workflow, Release Process workflow, Review Process workflow, Agent roles (PM, Architect, Coordinator, Implementer, Reviewer, QA, Reporter), Human approval gate (WAITING_APPROVAL, PILOT_FROZEN), Task state machine (NEW to REPORTED)

### Community 139 - "project-memory cluster"
Cohesion: 0.38
Nodes (7): Project Memory, PILOT_FROZEN activation state, config/autonomous-engineering.yaml, Scheduler Rules, docs/ai/autonomous-engineering.md, Work Orders (Tasks.md), Task Template

### Community 140 - "Community 140"
Cohesion: 0.29
Nodes (6): arrowParens, printWidth, $schema, semi, singleQuote, trailingComma

### Community 141 - "Community 141"
Cohesion: 0.38
Nodes (4): confirm(), handleTabChange(), openNewTab(), setup()

### Community 142 - "conftest cluster"
Cohesion: 0.43
Nodes (5): create_db_and_tables(), main(), global_function_setup2(), fixture, session_setup1()

### Community 143 - "Picamera2 Tests"
Cohesion: 0.33
Nodes (6): GroupBackend, GroupCameras, BaseModel, model_validator, Choose backends for still images/high quality images captured on main backend.…, transform non-discriminant config structure <v8 to new one. The new structure…

### Community 144 - "test_share cluster"
Cohesion: 0.48
Nodes (6): TestClient, test_get_limits_reset(), test_get_limits_reset_error(), test_get_limits_reset_nonexistant_failsilent(), test_get_stats_reset_all(), test_get_stats_reset_all_error()

### Community 145 - "AI Engineering Workflows"
Cohesion: 0.33
Nodes (6): Dependabot config (pip + github-actions, target dev), Pull request template, ai-gates CI workflow, benchmarks CI workflow, lint CI workflow, tests CI workflow (Python matrix)

### Community 147 - "Actions Config Group"
Cohesion: 0.33
Nodes (6): api_get_preview_image_filtered(), api_get_userselectable_filters(), get, get_plugin_avail_filters(), get_plugin_userselectable_filters(), test_pilgram_stage_get_filters()

### Community 148 - "test_information cluster"
Cohesion: 0.53
Nodes (5): TestClient, test_get_limits_reset(), test_get_limits_reset_error(), test_get_stats_reset(), test_get_stats_reset_all_error()

### Community 149 - "Media Collection Service"
Cohesion: 0.53
Nodes (5): TestClient, test_get_404_missing_item(), test_get_500_on_fail(), test_get_item_variants(), test_head_item()

### Community 150 - "test_static cluster"
Cohesion: 0.53
Nodes (5): TestClient, test_private_css(), test_private_css_nonexisting_placeholder(), test_read_web_sharepage(), test_read_web_spa()

### Community 151 - "Admin Files & Enumerate API"
Cohesion: 0.47
Nodes (4): test_get(), test_get_404_missing_item(), test_get_file_from_demofolder(), TestClient

### Community 152 - "test_tdd_lib cluster"
Cohesion: 0.50
Nodes (5): classify_changes(), entries: [{"status": "A"|"M"|"D"|"R087"..., "path": ...}] as from `git diff…, entry(), test_edge_classify_groups_each_kind(), test_edge_classify_ignores_deletes_and_pure_renames()

### Community 156 - "filter_pilgram2_test cluster"
Cohesion: 0.40
Nodes (4): filter_algo(), benchmark, fixture, test_pilgram_lores_benchmark()

### Community 157 - "test_enumerate cluster"
Cohesion: 0.60
Nodes (4): TestClient, test_admin_enumerate_files(), test_admin_enumerate_serialports(), test_admin_enumerate_usbcameras()

### Community 158 - "Community 158"
Cohesion: 0.50
Nodes (4): engines, node, npm, yarn

### Community 159 - "tdd_lib cluster"
Cohesion: 0.50
Nodes (4): parse_junit_failures(), Reads pytest --junitxml. A collection failure (usually a module that does not…, test_edge_junit_collection_failure_is_file_level(), test_error_parse_junit_failures_on_empty_or_invalid_xml()

### Community 160 - "GPIO Lights Plugin"
Cohesion: 0.67
Nodes (3): api_get_limitscounter_reset_all(), api_get_limitscounter_reset_field(), get

### Community 161 - "test_debug cluster"
Cohesion: 0.67
Nodes (3): TestClient, test_read_log(), test_read_log_err()

### Community 162 - "project-memory cluster"
Cohesion: 0.67
Nodes (3): Validation Auto-Fix Prompt, BLOCKED_HUMAN state, Bootstrap Repair Loop

## Ambiguous Edges - Review These
- `Plan: Pick-a-Booth v2 UI redesign` → `photobooth-frontend README`  [AMBIGUOUS]
  docs/plans/booth-redesign-v2.md · relation: conceptually_related_to

## Knowledge Gaps
- **400 isolated node(s):** `new-task-worktree.sh script`, `architect`, `product-manager`, `operating-model`, `Claude Code Runtime Rules` (+395 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **33 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Plan: Pick-a-Booth v2 UI redesign` and `photobooth-frontend README`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `BaseConfig` connect `baseconfig cluster` to `resilientservice cluster`, `Plugin Hookspecs & Stats`, `Commander Plugin`, `filter_pilgram2 cluster`, `DB Models & Alembic`, `Plugin Manager`, `Service Container Lifecycle`, `Plugin Hookspecs & Stats`, `Config Admin Tests`?**
  _High betweenness centrality (0.018) - this node is a cross-community bridge._
- **Why does `AbstractBackend` connect `Abstract Camera Backend` to `resilientservice cluster`, `digiCamControl Backend`, `Rclone Synchronizer`, `Abstract Camera Backend`, `PyAV Webcam Backend`, `Gphoto2 Backend`, `Picamera2 Tests`, `Wigglecam Backend`, `App Config & Acquisition Wiring`, `Picamera2 Tests`, `Backend Mode Controller`, `Picamera2 Backend`, `Acquisition Service`, `Virtual Camera Source`, `abstractbackend cluster`?**
  _High betweenness centrality (0.016) - this node is a cross-community bridge._
- **Why does `BaseService` connect `BaseService` to `Share Config Group`, `processing cluster`, `Container, Schemas & SSE`, `DB Models & Alembic`, `Logging Service`, `App Config & Acquisition Wiring`, `DB Models & Alembic`, `Plugin Manager`, `Processing Event Hooks`, `Information Service`, `Processing Service`, `gpio cluster`, `GPIO Pin Handling`, `share cluster`, `Acquisition Service`, `gpio cluster`, `Media Collection Service`?**
  _High betweenness centrality (0.015) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `AcquisitionService` (e.g. with `BaseService` and `InformationService`) actually correct?**
  _`AcquisitionService` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `AbstractBackend` (e.g. with `StoppableThread` and `DigicamcontrolBackend`) actually correct?**
  _`AbstractBackend` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `JobModelBase` (e.g. with `JobModelAnimation` and `CaptureSet`) actually correct?**
  _`JobModelBase` has 9 INFERRED edges - model-reasoned connections that need verification._