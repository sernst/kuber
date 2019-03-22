from kuber import helm_management


helm_management.render_helm_chart(
    chart_path='../samples/charts/prometheus'
)
