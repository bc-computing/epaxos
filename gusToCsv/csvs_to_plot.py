def csvs_to_plot():
    plot_script_file = os.path.join(plots_directory, '%s.gpi' % plot_name)
    generate_gnuplot_script_cdf(config, plot_script_file)
    run_gnuplot([plot_csv_file], os.path.join(plots_directory, '%s.png' % plot_name),
            plot_script_file)

    plot_script_file = os.path.join(plots_directory, '%s.gpi' % plot_name)
    generate_gnuplot_script_cdf_log(config, plot_script_file)
    run_gnuplot([plot_csv_file], os.path.join(plots_directory, '%s.png' % plot_name),
            plot_script_file)

