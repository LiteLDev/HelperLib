/// <reference path="../../index.d.ts" />

/**
 * @see https://github.com/LiteLDev/LiteLoaderBDS/blob/main/ScriptEngine/API/BaseAPI.cpp#L12
 * @see https://github.com/LiteLDev/LiteLoaderBDS/blob/main/LiteLoader/Header/MC/ActorDamageSource.hpp#L14
 */
declare enum DamageCause {
  ActorDamageCause_None = -0x01,
  ActorDamageCause_Override = 0x00,
  ActorDamageCause_Contact = 0x01,
  ActorDamageCause_EntityAttack = 0x02,
  ActorDamageCause_Projectile = 0x03,
  ActorDamageCause_Suffocation = 0x04,
  FActorDamageCause_all = 0x05,
  ActorDamageCause_Fire = 0x06,
  ActorDamageCause_FireTick = 0x07,
  ActorDamageCause_Lava = 0x08,
  ActorDamageCause_Drowning = 0x09,
  ActorDamageCause_BlockExplosion = 0x0a,
  ActorDamageCause_EntityExplosion = 0x0b,
  ActorDamageCause_Void = 0x0c,
  ActorDamageCause_Suicide = 0x0d,
  ActorDamageCause_Magic = 0x0e,
  ActorDamageCause_Wither = 0x0f,
  ActorDamageCause_Starve = 0x10,
  ActorDamageCause_Anvil = 0x11,
  ActorDamageCause_Thorns = 0x12,
  ActorDamageCause_FallingBlock = 0x13,
  ActorDamageCause_Piston = 0x14,
  ActorDamageCause_FlyIntoWall = 0x15,
  ActorDamageCause_Magma = 0x16,
  ActorDamageCause_Fireworks = 0x17,
  ActorDamageCause_Lightning = 0x18,
  ActorDamageCause_Charging = 0x19,
  ActorDamageCause_Temperature = 0x1a,
  ActorDamageCause_Freezing = 0x1b,
  ActorDamageCause_Stalactite = 0x1c,
  ActorDamageCause_Stalagmite = 0x1d,
  ActorDamageCause_All = 0x1f,
}
