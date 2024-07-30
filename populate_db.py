from pymongo import MongoClient
from config.database import workloads_collection


def insert_workloads(workloads):
    for workload in workloads:
        workloads_collection.insert_one(workload)
    print(f"Database populated with {len(workload)} systems.")

workloads = [
    {
        "Default_scenario": ["Windows (x86, ARM)", "Linux (x86, ARM)", "MacOS", "iOS", "Android"],
        "RunType": "SPEC CPU 2017",
        "Score": {"owner": "Sundar"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "spec_cpu_2017",
        "image": "spec_cpu_2017_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86)"],
        "RunType": "SPECworkstation 3.1",
        "Score": {"owner": "Jagan"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "specworkstation_3_1",
        "image": "specworkstation_3_1_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Linux"],
        "RunType": "SPECcloud",
        "Score": {"owner": "Sundar", "Q3'24": "~SPECCloud V1"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "speccloud",
        "image": "speccloud_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "upcoming"
    },
    {
        "Default_scenario": ["Linux"],
        "RunType": "SERT 2.x",
        "Score": {"owner": "Jagan"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "sert_2_x",
        "image": "sert_2_x_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Linux"],
        "RunType": "SPECpower_ssj 2008",
        "Score": {"owner": "Jagan"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "specpower_ssj_2008",
        "image": "specpower_ssj_2008_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86)"],
        "RunType": "SYSmark 30",
        "Score": {"owner": "Harish"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "sysmark_30",
        "image": "sysmark_30_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86)"],
        "RunType": "MobileMark 25",
        "Score": {"owner": "Harish"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "mobilemark_25",
        "image": "mobilemark_25_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86)"],
        "RunType": "CrossMark 1.0",
        "Score": {"owner": "Harish"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "crossmark_1_0",
        "image": "crossmark_1_0_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86, ARM)", "MacOS"],
        "RunType": "MLPerf - Client",
        "Score": {"owner": "Ramesh", "Q3'24": "MLPerf - Client 0.5"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "mlperf_client",
        "image": "mlperf_client_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "upcoming"
    },
    {
        "Default_scenario": ["Windows (x86, ARM)", "Linux", "MacOS", "iOS", "Android"],
        "RunType": "Geekbench 6.2",
        "Score": {"owner": "Max L/Aaron"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "geekbench_6_2",
        "image": "geekbench_6_2_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86, ARM)", "MacOS", "Linux", "Android"],
        "RunType": "Geekbench ML 0.6 Public Beta",
        "Score": {"owner": "Aaron/Max L"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "geekbench_ml_0_6",
        "image": "geekbench_ml_0_6_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "beta"
    },
    {
        "Default_scenario": ["Windows (x86, ARM)", "MacOS"],
        "RunType": "Procyon AI: Computer Vision",
        "Score": {"owner": "Aaron", "codename": "Redowa, Furlana"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "procyon_ai_cv",
        "image": "procyon_ai_cv_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86, ARM)"],
        "RunType": "Procyon AI: Image Generation",
        "Score": {"owner": "Aaron"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "procyon_ai_img_gen",
        "image": "procyon_ai_img_gen_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86, ARM)", "MacOS"],
        "RunType": "Procyon Office Productivity",
        "Score": {"owner": "Umar"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "procyon_office",
        "image": "procyon_office_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86)", "MacOS"],
        "RunType": "Procyon Photo Editing",
        "Score": {"owner": "Umar"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "procyon_photo",
        "image": "procyon_photo_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86)"],
        "RunType": "Procyon Video Editing",
        "Score": {"owner": "Umar"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "procyon_video",
        "image": "procyon_video_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86, ARM)", "MacOS"],
        "RunType": "Procyon 1-Hour Battery Life",
        "Score": {"owner": "Umar"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "procyon_battery",
        "image": "procyon_battery_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Varies by sub-test", "Windows (x86, ARM)", "MacOS", "iOS", "Android", "Linux"],
        "RunType": "3DMark for gaming PCs",
        "Score": {"owner": "Aaron", "subtests": "Speed Way (DX12 Ultimate), Time Spy (DX12), Time Spy Extreme (DX12 4K), Steel Nomad (X-platform replacement for Time Spy)"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "3dmark_gaming",
        "image": "3dmark_gaming_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86, ARM)", "MacOS", "iOS", "Android", "Linux"],
        "RunType": "3DMark for cross-platform",
        "Score": {"owner": "Aaron", "subtests": "Wild Life, Wild Life Extreme, Solar Bay"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "3dmark_cross_platform",
        "image": "3dmark_cross_platform_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86)"],
        "RunType": "3DMark CPU Test",
        "Score": {"owner": "Aaron"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "3dmark_cpu",
        "image": "3dmark_cpu_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86)", "MacOS"],
        "RunType": "PugetBench for Photoshop v1.0",
        "Score": {"owner": "Umar"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "pugetbench_photoshop",
        "image": "pugetbench_photoshop_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86)", "MacOS"],
        "RunType": "PugetBench for Premiere Pro v1.0",
        "Score": {"owner": "Umar"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "pugetbench_premiere",
        "image": "pugetbench_premiere_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86)"],
        "RunType": "PugetBench for Lightroom Classic 0.95",
        "Score": {"owner": "Umar"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "pugetbench_lightroom",
        "image": "pugetbench_lightroom_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86)", "MacOS"],
        "RunType": "PugetBench for After Effects 0.96.0",
        "Score": {"owner": "Umar"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "pugetbench_after_effects",
        "image": "pugetbench_after_effects_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86)", "MacOS"],
        "RunType": "PugetBench for DaVinci Resolve v1.0",
        "Score": {"owner": "Umar"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "pugetbench_davinci",
        "image": "pugetbench_davinci_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Not specified"],
        "RunType": "PassMark 11",
        "Score": {"owner": "Aaron"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "passmark_11",
        "image": "passmark_11_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86, ARM)", "Linux", "MacOS", "iOS", "Android"],
        "RunType": "WebXPRT 4",
        "Score": {"owner": "Mayura"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "webxprt_4",
        "image": "webxprt_4_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86, ARM)", "Linux", "MacOS", "iOS", "Android"],
        "RunType": "Speedometer 3",
        "Score": {"owner": "Mayura"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "speedometer_3",
        "image": "speedometer_3_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    },
    {
        "Default_scenario": ["Windows (x86, ARM)", "MacOS"],
        "RunType": "Cinebench 2024",
        "Score": {"owner": "Max L"},
        "Tools": None,
        "WorkloadVersion": None,
        "id": "cinebench_2024",
        "image": "cinebench_2024_image",
        "image_path": None,
        "iteration_number": "1",
        "status": "current"
    }
]

insert_workloads(workloads)
print("All systems have been inserted into the database.")