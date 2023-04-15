<script>
  import Router from "svelte-spa-router";
  import Home from "./routes/Home.svelte";
  import ReviewDetail from "./routes/ReviewDetail.svelte";

  const routes = {
    "/": Home,    // 주소에 매핑되는 컴포넌트로 <Home />을 등록했다. → Home.svelte
    "/detail/:review_id": ReviewDetail,   // 리뷰 상세
  };
</script>

<Router {routes} />
