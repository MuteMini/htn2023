import "vuetify/styles";
import { createVuetify, ThemeDefinition } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

const customTheme: ThemeDefinition = {
  dark: true,
  colors: {
    background: "#264653",
    surface: "#2A9D8F",
    primary: "#E9C46A",
    "primary-darken-1": "#D0B672",
    secondary: "#F4A261",
    "secondary-darken-1": "#C28654",
  },
};

export default createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: "myCustomLightTheme",
    themes: {
      myCustomLightTheme: customTheme,
    },
  },
});
