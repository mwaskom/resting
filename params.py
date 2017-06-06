base = dict(

    display_name="laptop",
    display_luminance=0,

    monitor_eye=True,

    fix_size=1,
    fix_color=0,
    fix_linewidth=5,

    run_duration=600,

)


scan = base.copy()
scan.update(

    display_name="cbi-propixx",
    trigger=["5"],
    wait_pre_run=12,
    draw_pre_run="fix",

)
