<template>
  <div
    id="app"
    class="container min-vh-100 d-flex align-items-center justify-content-center"
  >
    <main>
      <div class="row">
        <div class="header jumbotron my-5">
          <h1 class="display-4 text-center">Cool Tiny URL Clone</h1>
        </div>
        <div class="search-box">
          <input
            type="text"
            class="search-bar form-control form-control-lg"
            placeholder="Squash any URL here..."
            v-model="original_url"
            v-on:keyup.enter="fetchShortUrl"
          />
        </div>
        <div class="search-button d-grid gap-2 my-3">
          <button class="btn btn-primary" v-on:click="fetchShortUrl">
            Submit
          </button>
        </div>

        <div v-if="short_url!==''" class="short-url text-center mt-5 mb-4 pb-4 fs-3 font-monospace">
          Short Url:{{ url_base + short_url }}
        </div>

        <div class="statistics justify-content-center">
          <table class="table table-striped">
            <thead>
              <tr>
                <th style="text-align:center" scope="col">#</th>
                <th style="text-align:center" scope="col">Original URL</th>
                <th style="text-align:center" scope="col">Short Url</th>
                <th style="text-align:center" scope="col">Number of visits</th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="object in data">
                <th style="text-align:center" scope="row">{{ object.id }}</th>
                <td style="text-align:center">{{ object.original_url }}</td>
                <td style="text-align:center">{{ url_base + object.short_url }}</td>
                <td style="text-align:center">{{ object.visits }}</td>
              </tr>  
            </tbody>
   
          </table>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      url_base: window.location.origin + "/",
      backend_url: "http://127.0.0.1:5000",
      original_url: "",
      short_url: "",
      data: "",
      path_name: window.location.pathname,
    };
  },
  mounted: function() {

    this.fetchOriginalUrl(); //Calls the method to check for redirection
    this.fetchStatistic(); // Calls the method before page loads
  },
  computed: {
    getCurrentShortUrl() {
      return this.short_url !== "" ? "true" : "false";
    },
  },
  methods: {
    fetchShortUrl() {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: this.original_url }),
      };
      fetch(`${this.backend_url}/add_url`, requestOptions)
        .then((res) => {
          if (res.status !== 200) {
            this.original_url = "";
            console.log(
              "Looks like there was a problem. Status Code: " + res.status
            );
            return;
          } else {
            this.original_url = "";
            return res.json(); // returns unresolved Promise
          }
        })
        .then((data) => {
          this.short_url = data.data.new_url;
          this.original_url = "";
          this.fetchStatistic();
        });
    },

    fetchOriginalUrl() {
      fetch(`${this.backend_url}${this.path_name}`)
        .then((res) => {
          if (res.status !== 200) {
            console.log(
              "Looks like there was a problem. Status Code: " + res.status
            );
            return
          } else {
            return res.json(); // returns unresolved Promise
          }
        })
        .then((data) => {
          window.open(data.original_url, "_self");
        });
    },

    fetchStatistic() {
      fetch(`${this.backend_url}/stats`)
        .then((res) => {
          if (res.status !== 200) {
            console.log(
              "Looks like there was a problem. Status Code: " + res.status
            );
            return;
          } else {
            return res.json(); // returns unresolved Promise
          }
        })
        .then((data) => (this.data = data.data));
    },
  },
};
</script>

