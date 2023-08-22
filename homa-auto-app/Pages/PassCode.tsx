import React from "react";
import {
  Input,
  Stack,
  FormControl,
  Select,
  Button,
  Icon,
  Text,
} from "native-base";
import { Ionicons } from "@expo/vector-icons";
import Container from "../layout/container";

export default function PassCode() {
  const [text, setText] = React.useState("");
  const [select, setSelect] = React.useState("");
  const options = [
    "Lukman Abdulsalam",
    "Prof Uche",
    "Joseph Ibe",
    "Dr. Reginald",
  ];
  return (
    <Container title="Access Device">
      <Stack space={2} w={"100%"} px={4}>
        <Text>Input Pass Code for Front Door</Text>
        <FormControl>
          <Input
            p={2}
            colorScheme={"purple"}
            placeholder="MyPassword"
            value={text}
            type="password"
            onChangeText={(text) => setText(text)}
          />
        </FormControl>
        <Button
          rounded={"md"}
          variant={"solid"}
          rightIcon={<Icon as={<Ionicons name="arrow-forward" />} size="sm" />}
          colorScheme={"purple"}
        >
          Proceed
        </Button>
      </Stack>
    </Container>
  );
}
