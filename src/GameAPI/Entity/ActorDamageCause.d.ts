/// <reference path="../../index.d.ts" />

/**
 * @see {@linkcode Entity.hurt()}
 * @see [对实体造成伤害](https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/GameAPI/Entity?id=%e5%af%b9%e5%ae%9e%e4%bd%93%e9%80%a0%e6%88%90%e4%bc%a4%e5%ae%b3)
 * @see [LiteLoaderBDS/ScriptEngine/API/EntityAPI.cpp](https://github.com/LiteLDev/LiteLoaderBDS/blob/main/ScriptEngine/API/EntityAPI.cpp#L93)
 */
declare class ActorDamageCause {
  readonly Override = 0;

  readonly Contact = 1;

  readonly EntityAttack = 2;

  readonly Projectile = 3;

  readonly Suffocation = 4;

  readonly Fall = 5;

  readonly Fire = 6;

  readonly FireTick = 7;

  readonly Lava = 8;

  readonly Drowning = 9;

  readonly BlockExplosion = 10;

  readonly EntityExplosion = 11;

  readonly Void = 12;

  readonly Suicide = 13;

  readonly Magic = 14;

  readonly Wither = 15;

  readonly Starve = 16;

  readonly Anvil = 17;

  readonly Thorns = 18;

  readonly FallingBlock = 19;

  readonly Piston = 20;

  readonly FlyIntoWall = 21;

  readonly Magma = 22;

  readonly Fireworks = 23;

  readonly Lightning = 24;

  readonly Charging = 25;

  readonly Temperature = 26;

  readonly Freezing = 27;

  readonly Stalactite = 28;

  readonly Stalagmite = 29;
}
