import React from "react";

import { Input, Stack, FormControl, Select, Button, Icon } from "native-base";
import { Ionicons } from "@expo/vector-icons";
import Container from "../layout/container";

export default function CreateDevice() {
  const [text, setText] = React.useState("");
  const [select, setSelect] = React.useState("");
  const options = [
    "Lukman Abdulsalam",
    "Prof Uche",
    "Joseph Ibe",
    "Dr. Reginald",
  ];
  return (
    <Container title="Create Device">
      <Stack space={2} w={"100%"} px={4}>
        <FormControl>
          <FormControl.Label>Device Name</FormControl.Label>
          <Input
            p={2}
            colorScheme={"purple"}
            placeholder="Henry"
            value={text}
            onChangeText={(text) => setText(text)}
          />
        </FormControl>
        <FormControl>
          <FormControl.Label>Description</FormControl.Label>
          <Input
            p={2}
            colorScheme={"purple"}
            placeholder="My living room Socket"
            value={text}
            onChangeText={(text) => setText(text)}
          />
        </FormControl>
        <FormControl>
          <FormControl.Label>Owner</FormControl.Label>
          <Select
            placeholder="Select"
            selectedValue={select}
            onValueChange={(itemVal: string) => setSelect(itemVal)}
          >
            {options.map((item, index) => (
              <Select.Item key={index} label={item} value={item} />
            ))}
          </Select>
        </FormControl>
        <Button
          rounded={"md"}
          variant={"solid"}
          leftIcon={<Icon as={<Ionicons name="add" />} size="sm" />}
          colorScheme={"purple"}
        >
          Add New User
        </Button>
      </Stack>
    </Container>
  );
}
