import React from "react";
import { StatusBar } from "react-native";
import { NativeBaseProvider, Box, Text, HStack, Center } from "native-base";
import * as SplashScreen from "expo-splash-screen";
import {
  useFonts,
  Inter_500Medium,
  Inter_400Regular,
} from "@expo-google-fonts/inter";
import { Ionicons } from "@expo/vector-icons";
import { extendTheme } from "native-base";
import FooterButtton from "../components/FooterButton";

const newColorTheme = {
  brand: {
    900: "#8287af",
    800: "#7c83db",
    700: "#b3bef6",
  },
};
const theme = extendTheme({ colors: newColorTheme });

interface ContainerProps {
  title: string;
  children: React.ReactNode;
}

SplashScreen.preventAutoHideAsync();
export default function Container({ title, children }: ContainerProps) {
  const [selected, setSelected] = React.useState(0);

  const [fontsLoaded] = useFonts({
    Inter_500Medium,
    Inter_400Regular,
    ...Ionicons.font,
  });
  if (fontsLoaded) {
    return (
      <NativeBaseProvider theme={theme}>
        <StatusBar  backgroundColor={"purple"} barStyle="light-content" />
        <Box safeAreaTop bg={"purple.800"} />
        <HStack
          bg={"purple.800"}
          px={1}
          py={3}
          justifyContent="center"
          alignItems="center"
          w={"100%"}
        >
          <Text color={"white"} fontSize={20} fontWeight="bold">
            {title}
          </Text>
        </HStack>
        <Box flex={1} safeAreaTop width={"100%"} alignSelf={"center"}>
          <Center flex={1}>{children}</Center>
          <HStack
            bg={"purple.800"}
            alignItems={"center"}
            safeAreaBottom
            shadow={6}
          >
            <FooterButtton
              title={"Home"}
              iconName={"home"}
              selected={selected === 0}
              onPress={() => setSelected(0)}
            />
            <FooterButtton
              title={"Settings"}
              iconName={"settings"}
              selected={selected === 1}
              onPress={() => setSelected(1)}
            />
            <FooterButtton
              title={"My Devices"}
              iconName={"hardware-chip"}
              selected={selected === 2}
              onPress={() => setSelected(2)}
            />
            <FooterButtton
              title={"Users"}
              iconName={"person"}
              selected={selected === 3}
              onPress={() => setSelected(3)}
            />
          </HStack>
        </Box>
      </NativeBaseProvider>
    );
  } else {
    SplashScreen.hideAsync();
    return null;
  }
}
