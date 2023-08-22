import React from "react";
import Container from "../layout/container";
import { Button, ScrollView, Text, VStack, Icon } from "native-base";
import { CardItem } from "../components/CardItem";
import { Ionicons } from "@expo/vector-icons";


export default function DeviceList() {
  return (
    <Container title="My Devices">
      <Button
        my={3}
          rounded={"md"}
          variant={"solid"}
          rightIcon={<Icon as={<Ionicons name="add" />} size="sm" />}
          colorScheme={"purple"}
        >
          Add New Device
        </Button>
      <ScrollView w={"100%"} p={3} my={2}>
        <VStack flexWrap={"wrap"} space={3}>
          {[
            "Front Door",
            "Parlour Switch",
            "Main Gate",
            "Living Room Switch",
            "Living Room Socket",
          ].map((item, index) => (
            <CardItem key={index}>
              <Text>{item}</Text>
            </CardItem>
          ))}
        </VStack>
      </ScrollView>
    </Container>
  );
}
