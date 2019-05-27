export const Message1 = Vue.component("Message1-component", {
  template: `
  <button v-on:click='showLog'>Message1</button>
  `,
  methods: {
    showLog: function() {
      console.log("Message1");
    }
  }
});