//
//  AppData.m
//  ZhaoQiPei
//
//  Created by 找汽配ios开发 on 16/1/6.
//  Copyright © 2016年 祥运. All rights reserved.
//

#import "AppData.h"
#import "FMDatabase.h"

@interface AppData ()


@end

@implementation AppData

DEF_SINGLETON(AppData)

- (instancetype)init {
    self = [super init];
    if (self) {
        [self setupData];
    }
    return self;
}

- (void)dealloc {
    [self.databaseQueue close];
}

- (void)setupData {
    NSString * filePath = [[NSBundle mainBundle] pathForResource:@"Acupoint" ofType:@"db"];
    self.databaseQueue = [FMDatabaseQueue databaseQueueWithPath:filePath];
}

@end
