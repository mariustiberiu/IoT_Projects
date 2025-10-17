// Exemple Arduino - envoyer T et H simulés
void setup()
{
    Serial.begin(115200);
}
void loop()
{
    float t = random(180, 300) / 10.0; // 18.0 -> 30.0
    float h = random(400, 800) / 10.0; // 40 -> 80
    Serial.print("T:");
    Serial.print(t, 2);
    Serial.print(";H:");
    Serial.println(h, 2);
    delay(2000);
}