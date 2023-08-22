import React from "react";
import Container from "../layout/container";
import { ScrollView, Text, VStack } from "native-base";
import { CardItem } from "../components/CardItem";

export default function DeviceList() {
  return (
    <Container title="Home">
      <ScrollView w={"100%"} p={3}>
        <VStack flexWrap={"wrap"} space={3}>
          {["Card 1", "Card 2", "Card 3", "Card 4", "Card 5"].map(
            (item, index) => (
              <CardItem key={index}>
                <Text>{item}</Text>
              </CardItem>
            )
          )}
        </VStack>
      </ScrollView>
    </Container>
  );
}
