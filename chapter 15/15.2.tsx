This component works great for the happy path. One thing to consider:
if the API returns a 500 or the network times out, this will throw
an unhandled exception and crash the entire dashboard — not just
this chart.

Two options:

1. Wrap the fetch in a try/catch and render a fallback UI:

   try {
     const data = await fetchChartData(endpoint);
     setChartData(data);
   } catch (err) {
     setError("Unable to load chart data. Retry?");
   }

2. Add a React Error Boundary around this component so a failure
   here doesn't take down the whole page:

   <ErrorBoundary fallback={<ChartError />}>
     <DashboardChart endpoint={endpoint} />
   </ErrorBoundary>

Option 2 is generally better because it protects the parent
page even if we miss an error case inside the component.

The pattern: any component that fetches external data should
either handle its own errors or be wrapped in a boundary that
does. That way one flaky endpoint doesn't break everything.
