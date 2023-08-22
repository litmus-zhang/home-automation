import React from "react";

import {
  Input,
  Stack,
  FormControl,
  Select,
  Checkbox,
  Radio,
  Button,
  Icon,
} from "native-base";
import { Ionicons } from "@expo/vector-icons";

import Container from "../layout/container";

export default function CreateAccount() {
  const [text, setText] = React.useState("");
  const [select, setSelect] = React.useState("");
  const [checkbox, setCheckbox] = React.useState(false);
  const [radio, setRadio] = React.useState("");
  const options = ["User", "Admin"];

  return (
    <Container title="Create User">
      <Stack space={2} w={"100%"} px={4}>
        <FormControl>
          <FormControl.Label>Firstname</FormControl.Label>
          <Input
            p={2}
            colorScheme={"purple"}
            placeholder="Henry"
            value={text}
            onChangeText={(text) => setText(text)}
          />
        </FormControl>
        <FormControl>
          <FormControl.Label>Lastname</FormControl.Label>
          <Input
            p={2}
            colorScheme={"purple"}
            placeholder="Adebisi"
            value={text}
            onChangeText={(text) => setText(text)}
          />
        </FormControl>
        <FormControl>
          <FormControl.Label>Email</FormControl.Label>
          <Input
            p={2}
            colorScheme={"purple"}
            placeholder="Adebisihenry@gmail.com"
            type="text"
            value={text}
            onChangeText={(text) => setText(text)}
          />
        </FormControl>
        <FormControl>
          <FormControl.Label>Role</FormControl.Label>
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
